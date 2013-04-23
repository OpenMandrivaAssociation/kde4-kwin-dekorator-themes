Name:		kde4-kwin-dekorator-themes
Summary:	Themes for deKorator for KDE4
Version:	0.3
Release:	1
Group:		Graphical desktop/KDE
License:	GPL
Url:		http://www.kde-look.org/index.php?xcontentmode=21
# 23.04.2013
Source0:	all-themes-dekorator.tar.gz
BuildRequires:	kde4-macros
BuildArch:	noarch

%description
Themes for deKorator pack. Includes:
-Aero_Glass
-AlphaCube
-Area-51-Lte
-Area-51
-beo
-black-n-green
-Blended
-blue_sky
-Bushido-Yellow
-chunxiayu
-Clay
-clearLook1
-clearLook2
-clearLook3
-clearLook4
-ClearLooks2-Blue
-Default
-golden-wood-original
-golden-wood-thin
-Kde-max 0.2
-kore
-LinspireClear
-mapuna-blended
-matrix
-milknoir-0.3
-Mockup
-NuOrDER
-Orangio
-Phacile-blue
-Phacile-green
-Plastic
-S_Dark-0.1
-simple_deco
-The-Error
-Titan-5-Lt
-Vectorcell2b
-vista
-winclassic
-yet-another-deKorator

Get more themes at kde-look.org if you want.

%prep
# nothing

%build
# nothing

%install
mkdir -p %{buildroot}%{_kde_appsdir}/deKorator
pushd %{buildroot}%{_kde_appsdir}/deKorator
tar -xf %{SOURCE0}
rm -rf themes/Elementary
rm -rf themes/Kore
popd

%files
%defattr(644,root,root,755)
%{_kde_appsdir}/deKorator/themes/*

