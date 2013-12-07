# revision 16005
# category Package
# catalog-ctan /macros/latex/contrib/pauldoc
# catalog-date 2009-11-10 13:46:41 +0100
# catalog-license lppl
# catalog-version 0.5
Name:		texlive-pauldoc
Version:	0.5
Release:	6
Summary:	German LaTeX package documentation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pauldoc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pauldoc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pauldoc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pauldoc.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.5-2
+ Revision: 754722
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.5-1
+ Revision: 719207
- texlive-pauldoc
- texlive-pauldoc
- texlive-pauldoc
- texlive-pauldoc

