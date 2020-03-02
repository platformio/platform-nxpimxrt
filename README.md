# NXP i.MX RT: development platform for [PlatformIO](http://platformio.org)
[![Build Status](https://travis-ci.org/platformio/platform-nxpimxrt.svg?branch=develop)](https://travis-ci.org/platformio/platform-nxpimxrt)
[![Build status](https://ci.appveyor.com/api/projects/status/gm98eo04per1je25/branch/develop?svg=true)](https://ci.appveyor.com/project/ivankravets/platform-nxpimxrt/branch/develop)

The i.MX RT series of crossover processors features the Arm Cortex-M core, real-time functionality and MCU usability at a cost-effective price. Combining high performance with real-time functionality, the i.MX RT series of crossover processors are designed to support next-generation IoT applications with a high level of integration and security balanced with MCU-level usability.

* [Home](http://platformio.org/platforms/nxpimxrt) (home page in PlatformIO Platform Registry)
* [Documentation](http://docs.platformio.org/page/platforms/nxpimxrt.html) (advanced usage, packages, boards, frameworks, etc.)

# Usage

1. [Install PlatformIO](http://platformio.org)
2. Create PlatformIO project and configure a platform option in [platformio.ini](http://docs.platformio.org/page/projectconf.html) file:

## Stable version

```ini
[env:stable]
platform = nxpimxrt
board = ...
...
```

## Development version

```ini
[env:development]
platform = https://github.com/platformio/platform-nxpimxrt.git
board = ...
...
```

# Configuration

Please navigate to [documentation](http://docs.platformio.org/page/platforms/nxpimxrt.html).
