# revision 23324
# category Package
# catalog-ctan /macros/latex/contrib/biblatex
# catalog-date 2011-08-01 13:12:37 +0200
# catalog-license lppl
# catalog-version 1.6
Name:		texlive-biblatex
Version:	1.6
Release:	1
Summary:	Bibliographies in LaTeX using BibTeX for sorting only
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The biblatex package is a complete reimplementation of the
bibliographic facilities provided by LaTeX in conjunction with
BibTeX. It redesigns the way in which LaTeX interacts with
BibTeX at a fairly fundamental level. With biblatex, BibTeX is
only used (if it is used at all) to sort the bibliography and
to generate labels. Instead of being implemented in BibTeX's
style files, the formatting of the bibliography is entirely
controlled by TeX macros. Good working knowledge in LaTeX
should be sufficient to design new bibliography and citation
styles -- there is no need to learn BibTeX's postfix stack
language. Just like the bibliography styles, all citation
commands may be freely (re)defined. In fact, users need not
remain bound to BibTeX for use with biblatex: an alternative
bibliography processor biblatex-biber is available. Development
of biblatex and biblatex-biber is closely coupled; the present
release of biblatex is designed to work with biblatex-biber
version 0.9.3. The package needs e-TeX, and uses the author's
etoolbox and logreq packages. For users of biblatex-biber,
version 0.9 is required (at least; refer to the notes for the
version of biblatex-biber that you are using). Apart from the
features unique to biblatex, the package also incorporates core
features of the following packages: babelbib, bibtopic,
bibunits, chapterbib, cite, inlinebib, mcite and mciteplus,
mlbib, multibib, splitbib. There are also some conceptual
parallels to the natbib and amsrefs packages. The biblatex
package supports split bibliographies, multiple bibliographies
within one document, and separate lists of bibliographic
shorthands. Bibliographies may be subdivided into parts (by
chapter, by section, etc.) and/or segmented by topics (by type,
by keyword, etc.). The package is fully localized and can
interface with the babel package.

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
%{_texmfdistdir}/bibtex/bib/biblatex/biblatex-examples.bib
%{_texmfdistdir}/bibtex/bst/biblatex/biblatex.bst
%{_texmfdistdir}/bibtex/csf/biblatex/latin1.csf
%{_texmfdistdir}/bibtex/csf/biblatex/latin1_at.csf
%{_texmfdistdir}/bibtex/csf/biblatex/latin1_de.csf
%{_texmfdistdir}/bibtex/csf/biblatex/latin1_dk.csf
%{_texmfdistdir}/bibtex/csf/biblatex/latin1_fi.csf
%{_texmfdistdir}/bibtex/csf/biblatex/latin1_no.csf
%{_texmfdistdir}/bibtex/csf/biblatex/latin1_se.csf
%{_texmfdistdir}/bibtex/csf/biblatex/latin9.csf
%{_texmfdistdir}/bibtex/csf/biblatex/latin9_at.csf
%{_texmfdistdir}/bibtex/csf/biblatex/latin9_de.csf
%{_texmfdistdir}/bibtex/csf/biblatex/latin9_dk.csf
%{_texmfdistdir}/bibtex/csf/biblatex/latin9_fi.csf
%{_texmfdistdir}/bibtex/csf/biblatex/latin9_no.csf
%{_texmfdistdir}/bibtex/csf/biblatex/latin9_se.csf
%{_texmfdistdir}/bibtex/csf/biblatex/winansi.csf
%{_texmfdistdir}/bibtex/csf/biblatex/winansi_at.csf
%{_texmfdistdir}/bibtex/csf/biblatex/winansi_de.csf
%{_texmfdistdir}/bibtex/csf/biblatex/winansi_dk.csf
%{_texmfdistdir}/bibtex/csf/biblatex/winansi_fi.csf
%{_texmfdistdir}/bibtex/csf/biblatex/winansi_no.csf
%{_texmfdistdir}/bibtex/csf/biblatex/winansi_se.csf
%{_texmfdistdir}/tex/latex/biblatex/bbx/alphabetic-verb.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/alphabetic.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/authortitle-comp.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/authortitle-ibid.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/authortitle-icomp.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/authortitle-tcomp.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/authortitle-terse.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/authortitle-ticomp.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/authortitle.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/authoryear-comp.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/authoryear-ibid.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/authoryear-icomp.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/authoryear.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/debug.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/draft.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/numeric-comp.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/numeric-verb.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/numeric.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/reading.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/standard.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/verbose-ibid.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/verbose-inote.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/verbose-note.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/verbose-trad1.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/verbose-trad2.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/verbose-trad3.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/verbose.bbx
%{_texmfdistdir}/tex/latex/biblatex/biblatex.cfg
%{_texmfdistdir}/tex/latex/biblatex/biblatex.def
%{_texmfdistdir}/tex/latex/biblatex/biblatex.sty
%{_texmfdistdir}/tex/latex/biblatex/blx-compat.def
%{_texmfdistdir}/tex/latex/biblatex/blx-mcite.def
%{_texmfdistdir}/tex/latex/biblatex/blx-natbib.def
%{_texmfdistdir}/tex/latex/biblatex/cbx/alphabetic-verb.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/alphabetic.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/authortitle-comp.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/authortitle-ibid.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/authortitle-icomp.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/authortitle-tcomp.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/authortitle-terse.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/authortitle-ticomp.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/authortitle.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/authoryear-comp.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/authoryear-ibid.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/authoryear-icomp.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/authoryear.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/debug.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/draft.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/numeric-comp.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/numeric-verb.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/numeric.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/reading.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/verbose-ibid.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/verbose-inote.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/verbose-note.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/verbose-trad1.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/verbose-trad2.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/verbose-trad3.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/verbose.cbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/UKenglish.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/USenglish.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/american.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/australian.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/austrian.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/brazil.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/brazilian.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/british.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/canadian.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/danish.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/dutch.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/english.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/finnish.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/french.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/german.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/greek.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/italian.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/naustrian.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/newzealand.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/ngerman.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/norsk.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/norwegian.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/nynorsk.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/portuges.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/portuguese.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/spanish.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/swedish.lbx
%doc %{_texmfdistdir}/doc/latex/biblatex/README
%doc %{_texmfdistdir}/doc/latex/biblatex/RELEASE
%doc %{_texmfdistdir}/doc/latex/biblatex/biblatex.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/biblatex.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/01-introduction.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/01-introduction.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/02-annotations.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/02-annotations.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/10-references-per-section.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/10-references-per-section.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/11-references-by-section.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/11-references-by-section.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/12-references-by-segment.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/12-references-by-segment.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/13-references-by-keyword.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/13-references-by-keyword.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/14-references-by-category.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/14-references-by-category.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/15-references-by-type.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/15-references-by-type.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/16-numeric-prefixed-1.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/16-numeric-prefixed-1.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/17-numeric-prefixed-2.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/17-numeric-prefixed-2.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/18-numeric-hybrid.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/18-numeric-hybrid.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/19-alphabetic-prefixed.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/19-alphabetic-prefixed.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/20-indexing-basic.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/20-indexing-basic.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/21-indexing-advanced.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/21-indexing-advanced.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/30-style-numeric.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/30-style-numeric.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/31-style-numeric-comp.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/31-style-numeric-comp.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/32-style-numeric-verb.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/32-style-numeric-verb.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/40-style-alphabetic.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/40-style-alphabetic.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/41-style-alphabetic-verb.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/41-style-alphabetic-verb.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/50-style-authoryear.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/50-style-authoryear.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/51-style-authoryear-ibid.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/51-style-authoryear-ibid.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/52-style-authoryear-comp.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/52-style-authoryear-comp.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/53-style-authoryear-icomp.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/53-style-authoryear-icomp.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/60-style-authortitle.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/60-style-authortitle.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/61-style-authortitle-ibid.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/61-style-authortitle-ibid.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/62-style-authortitle-comp.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/62-style-authortitle-comp.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/63-style-authortitle-icomp.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/63-style-authortitle-icomp.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/64-style-authortitle-terse.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/64-style-authortitle-terse.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/65-style-authortitle-tcomp.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/65-style-authortitle-tcomp.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/66-style-authortitle-ticomp.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/66-style-authortitle-ticomp.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/70-style-verbose.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/70-style-verbose.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/71-style-verbose-ibid.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/71-style-verbose-ibid.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/72-style-verbose-note.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/72-style-verbose-note.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/73-style-verbose-inote.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/73-style-verbose-inote.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/74-style-verbose-trad1.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/74-style-verbose-trad1.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/75-style-verbose-trad2.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/75-style-verbose-trad2.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/76-style-verbose-trad3.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/76-style-verbose-trad3.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/80-style-reading.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/80-style-reading.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/81-style-draft.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/81-style-draft.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/82-style-debug.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/82-style-debug.tex
%doc %{_texmfdistdir}/doc/latex/biblatex/examples/biblatex-examples.bib
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
