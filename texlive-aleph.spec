Name:		texlive-aleph
Version:	RC2
Release:	1
Summary:	Extended TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/aleph
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aleph.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aleph.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-latex
Requires:	texlive-plain
Requires:	texlive-aleph.bin
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Requires(post):	texlive-tetex

%description
An development of omega, using most of the extensions of TeX
itself developed for e-TeX.

%pre
    %_texmf_mktexlsr_pre

%post
sed -i	-e 's/^#! \(aleph aleph \- \*aleph.ini\)/\1/'	\
	-e 's/^#! \(lamed aleph language.dat \*lambda.ini\)/\1/'	\
	%{_texmfdir}/web2c/fmtutil.cnf

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	if [ -f %{_texmfdir}/web2c/fmtutil.cnf ]; then
	    sed -i  -e 's/^\(aleph aleph \- \*aleph.ini\)/#! \1/'	\
		    -e 's/^\(lamed aleph language.dat \*lambda.ini\)/#! \1/'	\
		%{_texmfdir}/web2c/fmtutil.cnf
	fi
    fi

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/aleph/base/News
%doc %{_texmfdistdir}/doc/aleph/base/readme.txt
%doc %{_mandir}/man1/aleph.1*
%doc %{_texmfdir}/doc/man/man1/aleph.man1.pdf
%doc %{_mandir}/man1/lamed.1*
%doc %{_texmfdir}/doc/man/man1/lamed.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
