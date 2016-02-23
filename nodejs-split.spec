%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

# Disabled as BR: for tests are not in fedora
%global enable_tests 0

%global module_name split

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        0.3.3
Release:        6%{?dist}
Summary:        Split a text stream into a line stream

License:        MIT
URL:            https://github.com/dominictarr/split
Source0:        http://registry.npmjs.org/%{module_name}/-/%{module_name}-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs010-runtime

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(asynct)
BuildRequires:  %{?scl_prefix}npm(it-is)
BuildRequires:  %{?scl_prefix}npm(ubelt)
BuildRequires:  %{?scl_prefix}npm(stream-spec)
BuildRequires:  %{?scl_prefix}npm(event-stream)
BuildRequires:  %{?scl_prefix}npm(string-to-stream)
%endif

%description
Break up a stream and reassemble it so that each line is a chunk.
matcher may be a String, or a RegExp.

%prep
%setup -q -n package
rm -rf node_modules

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/%{module_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
asynct test
%endif

%files
%doc readme.markdown LICENCE examples
%{nodejs_sitelib}/%{module_name}

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.3.3-6
- rebuilt

* Fri Jan 15 2016 Tomas Hrcka <thrcka@redhat.com> - 0.3.3-5
- Enable find_provides_and_requires macro

* Thu Jan 07 2016 Tomas Hrcka <thrcka@redhat.com> - 0.3.3-3
- Enable scl macros

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb 12 2015 Parag Nemade <pnemade AT redhat DOT com> - 0.3.3-1
- update to 0.3.3 upstream release

* Tue Dec 09 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.3.2-1
- Initial packaging
