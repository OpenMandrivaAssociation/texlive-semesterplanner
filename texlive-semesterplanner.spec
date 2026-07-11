%global tl_name semesterplanner
%global tl_revision 56841

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Create beautiful semester timetables and more
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/semesterplanner
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/semesterplanner.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/semesterplanner.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/semesterplanner.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package defines several useful environments for a beautiful
printable semester plan. It includes a timetable (which is using the
schedule-Package) as well as appointments, deadlines, and exams. The
package requires color, TikZ, schedule, and fontawesome. Furthermore,
documents need to be compiled with LuaLaTeX.

