%global tl_name aleph
%global tl_revision 77830

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Extended TeX
Group:		Publishing
URL:		https://www.ctan.org/pkg/aleph
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aleph.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aleph.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Requires:	texlive(aleph.bin)
Requires:	texlive(cm)
Requires:	texlive(hyphen-base)
Requires:	texlive(knuth-lib)
Requires:	texlive(lambda)
Requires:	texlive(latex)
Requires:	texlive(plain)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
An development of omega, using most of the extensions of TeX itself
developed for e-TeX.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist/doc
%dir %{_datadir}/texmf-dist/texmf-dist/doc/aleph
%dir %{_datadir}/texmf-dist/texmf-dist/doc/man
%dir %{_datadir}/texmf-dist/texmf-dist/doc/aleph/base
%dir %{_datadir}/texmf-dist/texmf-dist/doc/man/man1
%doc %{_datadir}/texmf-dist/texmf-dist/doc/aleph/base/ChangeLog
%doc %{_datadir}/texmf-dist/texmf-dist/doc/aleph/base/News
%doc %{_datadir}/texmf-dist/texmf-dist/doc/aleph/base/readme.txt
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/aleph.1
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/aleph.man1.pdf
