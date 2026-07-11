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
BuildSystem:	texlive
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

