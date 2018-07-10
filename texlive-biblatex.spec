Name:		texlive-biblatex
Version:	3.11
Release:	2
Summary:	Bibliographies in LaTeX using BibTeX for sorting only
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Biblatex is a complete reimplementation of the bibliographic
facilities provided by LaTeX in conjunction with BibTeX. It
redesigns the way in which LaTeX interacts with BibTeX at a
fairly fundamental level. With biblatex, BibTeX is only used
(if it is used at all) to sort the bibliography and to generate
labels. Formatting of the bibliography is entirely controlled
by TeX macros (the BibTeX-based mechanism embeds some parts of
formatting in the BibTeX style file. Good working knowledge in
LaTeX should be sufficient to design new bibliography and
citation styles; nothing related to BibTeX's language is
needed. In fact, users need not remain bound to BibTeX for use
with biblatex: an alternative bibliography processor biblatex-
biber is available. Development of biblatex and biblatex-biber
is closely coupled; the present release of biblatex is designed
to work with biblatex-biber version 0.9.6. The package needs e-
TeX, and uses the author's etoolbox and logreq packages. For
users of biblatex-biber, version 0.9 is required (at least;
refer to the notes for the version of biblatex-biber that you
are using). Apart from the features unique to biblatex, the
package also incorporates core features of the following
packages: babelbib, bibtopic, bibunits, chapterbib, cite,
inlinebib, mcite and mciteplus, mlbib, multibib, splitbib.
Biblatex supports split bibliographies and multiple
bibliographies within one document, and separate lists of
bibliographic shorthands. Bibliographies may be subdivided into
parts (by chapter, by section, etc.) and/or segmented by topics
(by type, by keyword, etc.). Biblatex is fully localized and
can interface with the babel.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/biblatex
%{_texmfdistdir}/bibtex/bst/biblatex
%{_texmfdistdir}/tex/latex/biblatex
%doc %{_texmfdistdir}/doc/latex/biblatex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
