# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%global parent plexus
%global subname interactivity

Name:           plexus-interactivity
Version:        1.0
Release:        0.13.alpha6%{?dist}
Epoch:          0
Summary:        Plexus Interactivity Handler Component
License:        MIT
URL:            http://plexus.codehaus.org/
# svn export \
#   http://svn.codehaus.org/plexus/plexus-components/tags/plexus-interactivity-1.0-alpha-6/
# tar caf plexus-interactivity-1.0-alpha-6-src.tar.xz \
#   plexus-interactivity-1.0-alpha-6
Source0:        plexus-interactivity-1.0-alpha-6-src.tar.xz
Patch1:         plexus-interactivity-dependencies.patch

BuildArch:      noarch
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  ant >= 0:1.6
BuildRequires:  maven-local
BuildRequires:  maven-resources-plugin
BuildRequires:  jline
BuildRequires:  plexus-utils
BuildRequires:  plexus-component-api

%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n plexus-interactivity-1.0-alpha-6
%patch1 -p1

%mvn_file :plexus-{*} plexus/@1

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%files javadoc -f .mfiles-javadoc

%changelog
* Fri Aug 16 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.0-0.13.alpha6
- Migrate away from mvn-rpmbuild (#997434)

* Fri Jul 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-0.12.alpha6
- Remove workaround for rpm bug #646523

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-0.11.alpha6
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.10.alpha6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0:1.0-0.9.alpha6
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Dec 11 2012 Michal Srb <msrb@redhat.com> - 0:1.0-0.8.alpha6
- Removed dependency on plexus-container-default (Resolves: #878573)
- Fixed rpmlint warning

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.7.alpha6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May  2 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.0-0.6.alpha6
- Add patch to fix build issues

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.5.a6.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 29 2011 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.4.a6.8
- Build with maven 3.
- Adapt to current guidelines.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.4.a6.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec  1 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.0-0.3.a6.7
- Fix pom filenames (Resolves rhbz#655821)
- Cleanups according to new guidelines

* Wed Oct 6 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.3.a6.6
- Use javadoc:aggregate.

* Wed Jul 21 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.3.a6.5
- Really fix depmaps.

* Wed Jul 21 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.3.a6.4
- Add parent/subname defines to fix poms/depmaps.

* Wed Jul 21 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.3.a6.3
- Update to alpha 6.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.3.a5.2.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.2.a5.2.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.0-0.1.a5.2.3
- drop repotag
- fix license tag

* Tue Mar 13 2007 Matt Wringe <mwringe@redhat.com> 1.0-0.1.a5.2jpp.2
- Add missing build requires for ant-nodeps

* Fri Feb 16 2007 Andrew Overholt <overholt@redhat.com> 1.0-0.1.a5.2jpp.1
- Remove javadoc symlinking

* Thu Feb 23 2006 Fernando Nasser <fnasser@redhat.com> - 0:1.0-0.a5.2jpp
- First JPP 1.7 build
- With remavenization to 1.1 by Deepak Bhole <dbhole@redhat.com>

* Mon Nov 07 2005 Ralph Apel <r.apel at r-apel.de> - 0:1.0-0.a5.1jpp
- First JPackage build
