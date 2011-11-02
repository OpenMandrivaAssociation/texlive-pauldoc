Name:		texlive-pauldoc
Version:	0.5
Release:	1
Summary:	German LaTeX package documentation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pauldoc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pauldoc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pauldoc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pauldoc.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The pauldoc package provides helpers for German language
package documentation.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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