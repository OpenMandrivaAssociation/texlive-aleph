# revision 26689
# category Package
# catalog-ctan /systems/aleph
# catalog-date 2012-02-09 23:17:52 +0100
# catalog-license gpl
# catalog-version RC2
Name:		texlive-aleph
Version:	RC2
Release:	7
Summary:	Extended TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/aleph
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aleph.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aleph.doc.tar.xz
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
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/aleph <<EOF
#
# from aleph:
aleph aleph - *aleph.ini
lamed aleph language.dat *lambda.ini
EOF


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> RC2-6
+ Revision: 811955
- Update to latest release.

* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> RC2-5
+ Revision: 804448
- Update to latest release.

* Tue Feb 21 2012 Paulo Andrade <pcpa@mandriva.com.br> RC2-4
+ Revision: 778422
- Rebuild after tlpobj2spec.pl bug correction.

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> RC2-3
+ Revision: 749156
- Rebuild to reduce used resources

* Tue Nov 08 2011 Paulo Andrade <pcpa@mandriva.com.br> RC2-2
+ Revision: 729089
- texlive-aleph

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> RC2-1
+ Revision: 717809
- texlive-aleph
- texlive-aleph
- texlive-aleph
- texlive-aleph
- texlive-aleph
- texlive-aleph

