########################################################################################

%define _logdir           %{_localstatedir}/log
%define _rundir           %{_localstatedir}/run
%define _lockdir          %{_localstatedir}/lock

%define _loc_prefix       %{_prefix}/local
%define _loc_exec_prefix  %{_loc_prefix}
%define _loc_bindir       %{_loc_exec_prefix}/bin
%define _loc_libdir       %{_loc_exec_prefix}/%{_lib}
%define _loc_libexecdir   %{_loc_exec_prefix}/libexec
%define _loc_sbindir      %{_loc_exec_prefix}/sbin
%define _loc_bindir       %{_loc_exec_prefix}/bin
%define _loc_datarootdir  %{_loc_prefix}/share
%define _loc_datadir      %{_loc_datarootdir}
%define _loc_includedir   %{_loc_prefix}/include

########################################################################################

Summary:            Creates a set of static HTML pages in a yum repository
Name:               repoview-kaos
Version:            0.6.6
Release:            6%{?dist}
License:            GPLv2+
Group:              Applications/System
URL:                http://essentialkaos.com
Vendor:             ESSENTIAL KAOS

Source0:            %{name}-%{version}.tar.bz2

BuildArch:          noarch
BuildRoot:          %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:           python-kid >= 0.6.3 yum >= 3.0 python >= 2.5

Provides:           %{name} = %{version}-%{release}

########################################################################################

%description
RepoView creates a set of static HTML pages in a yum repository for easy
browsing.

########################################################################################

%prep
%setup -q
%build

%install
rm -rf %{buildroot}

install -dm 755 %{buildroot}%{_datadir}/%{name}
install -dm 755 %{buildroot}%{_bindir}
install -dm 755 %{buildroot}%{_mandir}/man8

install -pm 755 repoview.py %{buildroot}%{_bindir}/%{name}
install -pm 644 repoview.8 %{buildroot}%{_mandir}/man8/repoview-kaos.8
install -pm 644 repoview.8 %{buildroot}%{_mandir}/man8/repoview.8

cp -rp templates %{buildroot}%{_datadir}/%{name}/

%post 
if [[ $1 -eq 1 ]] ; then
  ln -s %{_bindir}/%{name} %{_bindir}/repoview
  ln -s %{_datadir}/%{name}/templates/kaos \
        %{_datadir}/%{name}/templates/default
fi

%postun
if [[ $1 -eq 0 ]] ; then
  rm -f %{_bindir}/repoview
  rm -f %{_datadir}/%{name}/templates/default
fi

%clean
rm -rf %{buildroot}

########################################################################################

%files
%defattr(-, root, root, -)
%doc README.md COPYING
%{_datadir}/%{name}
%{_bindir}/*
%{_mandir}/man*/*

########################################################################################

%changelog
* Fri Feb 19 2016 Anton Novojilov <andy@essentialkaos.com> - 0.6.6-6
- Using Google Fonts for serving Open Sans font
- Removed minified css

* Tue Jan 15 2013 Anton Novojilov <andy@essentialkaos.com> - 0.6.6-5
- Updated templates to more light UI
- Changed main font to Open Sans

* Thu Jun 21 2012 Anton Novojilov <andy@essentialkaos.com> - 0.6.6-4
- Changed binary and data dir name
- Added international template
- Changed template dir structure

* Tue Jun 12 2012 Anton Novojilov <andy@essentialkaos.com> - 0.6.6-3
- Added Ubuntu webfonts
- Minimized css
- Some UI improvements for clear view and fast page rendering

* Thu Jun 7 2012 Anton Novojilov <andy@essentialkaos.com> - 0.6.6-2
- Totally changed UI
- Added logo

* Wed Nov 16 2011 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6.6-1
- Update to 0.6.6 (bugfixes)

* Fri Feb 19 2010 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6.5-1
- Update to 0.6.5 (bugfixes)

* Wed Jan 27 2010 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6.4-1
- Update to 0.6.4 (bugfixes)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 27 2009 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6.3-1
- Upstream 0.6.3
- Upstream fix for mixed-case packages and md5 warnings (obsoletes patch)
- Minor fixes to functionality

* Thu Mar 26 2009 Seth Vidal <skvidal at fedoraproject.org>
- don't lowercase pkgnames
- stop md5 warning emit

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 02 2008 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6.2-1
- Upstream 0.6.2
- Modify URLs to point to the new repoview home

* Thu Oct 25 2007 Seth Vidal <skvidal at fedoraproject.org> - 0.6.1-2
- add fedora repoview templates

* Thu Sep 27 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6.1-1
- Upstream 0.6.1
- Adjust license to GPLv2+

* Thu Jul 19 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6.0-1
- Upstream 0.6.0
- Drop obsolete patch

* Tue Jul 04 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.5.2-1
- Version 0.5.2
- Use yum-2.9 API patch (Jesse Keating)

* Wed Feb 15 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.5.1-1
- Version 0.5.1

* Fri Jan 13 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.5-1
- Version 0.5

* Sun Oct 09 2005 Konstantin Ryabitsev <icon@linux.duke.edu> - 0.4.1-1
- Version 0.4.1

* Fri Sep 23 2005 Konstantin Ryabitsev <icon@linux.duke.edu> - 0.4-1
- Version 0.4
- Require yum >= 2.3
- Drop requirement for python-elementtree, since it's required by yum
- Disttagging.

* Mon Apr 04 2005 Konstantin Ryabitsev <icon@linux.duke.edu> 0.3-3
- Do not BuildRequire sed -- basic enough dependency, even for version 4.

* Tue Mar 29 2005 Konstantin Ryabitsev <icon@linux.duke.edu> 0.3-2
- Preserve timestamps on installed files
- Do not use macros in source tags
- Omit Epoch

* Fri Mar 25 2005 Konstantin Ryabitsev <icon@linux.duke.edu> 0.3-1
- Version 0.3

* Thu Mar 10 2005 Konstantin Ryabitsev <icon@linux.duke.edu> 0.2-1
- Version 0.2
- Fix URL
- Comply with fedora extras specfile format.
- Depend on python-elementtree and python-kid -- the names in extras.

* Thu Mar 03 2005 Konstantin Ryabitsev <icon@linux.duke.edu> 0.1-1
- Initial build