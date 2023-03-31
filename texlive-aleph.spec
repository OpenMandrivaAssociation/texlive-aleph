Name:		texlive-aleph
Version:	62387
Release:	2
Summary:	Extended TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/aleph
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aleph.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aleph.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-tetex
Requires:	texlive-latex
Requires:	texlive-plain
Requires:	texlive-lambda
Requires:	texlive-aleph.bin

%description
An development of omega, using most of the extensions of TeX
itself developed for e-TeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	rm -fr %{_texmfvardir}/web2c/aleph
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%_texmf_fmtutil_d/aleph
%doc %{_texmfdistdir}/doc/aleph/base/News
%doc %{_texmfdistdir}/doc/aleph/base/readme.txt
%doc %{_mandir}/man1/aleph.1*
%doc %{_texmfdistdir}/doc/man/man1/aleph.man1.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/aleph <<EOF
#
# from aleph:
aleph aleph - *aleph.ini
lamed aleph language.dat *lambda.ini
EOF
