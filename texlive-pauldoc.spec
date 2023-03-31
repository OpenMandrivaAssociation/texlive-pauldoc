Name:		texlive-pauldoc
Version:	16005
Release:	2
Summary:	German LaTeX package documentation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pauldoc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pauldoc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pauldoc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pauldoc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The pauldoc package provides helpers for German language
package documentation.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pauldoc/pauldoc.sty
%doc %{_texmfdistdir}/doc/latex/pauldoc/README
%doc %{_texmfdistdir}/doc/latex/pauldoc/pauldoc.pdf
#- source
%doc %{_texmfdistdir}/source/latex/pauldoc/pauldoc.dtx
%doc %{_texmfdistdir}/source/latex/pauldoc/pauldoc.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
