# revision 23409
# category Package
# catalog-ctan /systems/aleph
# catalog-date 2009-11-09 13:03:38 +0100
# catalog-license gpl
# catalog-version RC2
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
    %_texmf_fmtutil_pre

%post
    %_texmf_fmtutil_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_fmtutil_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_fmtutil_post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_fmtutil_d/aleph
%doc %{_texmfdistdir}/doc/aleph/base/News
%doc %{_texmfdistdir}/doc/aleph/base/readme.txt
%doc %{_mandir}/man1/aleph.1*
%doc %{_texmfdir}/doc/man/man1/aleph.man1.pdf
%doc %{_mandir}/man1/lamed.1*
%doc %{_texmfdir}/doc/man/man1/lamed.man1.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/aleph <<EOF
aleph aleph - *aleph.ini
lamed aleph language.dat *lambda.ini
EOF
