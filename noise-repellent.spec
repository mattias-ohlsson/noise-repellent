Name:           noise-repellent
Version:        0.1.5
Release:        1%{?dist}
Summary:        An LV2 plugin for noise reduction

License:        LGPLv3+
URL:            https://github.com/lucianodato/noise-repellent

Source0:        https://github.com/lucianodato/noise-repellent/archive/%{version}.tar.gz

# https://github.com/lucianodato/noise-repellent/issues/68
Patch0:         https://github.com/lucianodato/noise-repellent/commit/a88e8125aaa87fa91e5cb4fc937c2ad0fe2e2817.patch
Patch1:         https://github.com/lucianodato/noise-repellent/commit/7f5a8fbef48fed75b9168509a4e3f985ae878988.patch

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  fftw-devel
BuildRequires:  lv2-devel

%description
An LV2 plug-in for broadband noise reduction with spectral gating and adaptive
noise thresholds estimation.

%package -n lv2-%{name}-plugins
Summary:        Noise Repellent LV2 plugin

%description -n lv2-%{name}-plugins
An LV2 plug-in for broadband noise reduction with spectral gating and adaptive
noise thresholds estimation.

This package contains the LV2 plugin.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files -n lv2-%{name}-plugins
%license LICENSE
%doc README.md
%{_libdir}/lv2/nrepel.lv2

%changelog
* Wed Nov 11 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 0.1.5-1
- Initial build
