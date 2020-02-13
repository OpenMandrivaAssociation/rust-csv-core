# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate csv-core

Name:           rust-%{crate}
Version:        0.1.6
Release:        4%{?dist}
Summary:        Bare bones CSV parsing with no_std support

# Upstream license specification: Unlicense/MIT
License:        Unlicense or MIT
URL:            https://crates.io/crates/csv-core
Source:         %{crates_source}
# Initial patched metadata
# - Bump arrayvec to 0.5 https://github.com/BurntSushi/rust-csv/pull/182
Patch0:         csv-core-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Bare bones CSV parsing with no_std support.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license COPYING LICENSE-MIT UNLICENSE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+libc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libc-devel %{_description}

This package contains library source intended for building other packages
which use "libc" feature of "%{crate}" crate.

%files       -n %{name}+libc-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 06 17:39:06 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.6-3
- Bump arrayvec to 0.5

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 07:27:47 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.6-1
- Update to 0.1.6

* Sat Jun 22 13:08:27 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.5-4
- Regenerate

* Sun Jun 09 15:39:10 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.5-3
- Regenerate

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Josh Stone <jistone@redhat.com> - 0.1.5-1
- Update to 0.1.5

* Sat Nov 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-4
- Fix summary

* Fri Nov 09 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.4-3
- Adapt to new packaging

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-1
- Initial package
