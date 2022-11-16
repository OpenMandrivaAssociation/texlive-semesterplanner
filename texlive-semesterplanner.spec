Name:		texlive-semesterplanner
Version:	56841
Release:	1
Summary:	Create beautiful semester timetables and more
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/semesterplanner
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semesterplanner.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semesterplanner.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semesterplanner.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package defines several useful environments for a
beautiful printable semester plan. It includes a timetable
(which is using the schedule-Package) as well as appointments,
deadlines, and exams. The package requires color, TikZ,
schedule, and fontawesome. Furthermore, documents need to be
compiled with LuaLaTeX.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/lualatex/semesterplanner
%{_texmfdistdir}/tex/lualatex/semesterplanner
%doc %{_texmfdistdir}/doc/lualatex/semesterplanner

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
