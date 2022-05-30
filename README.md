# NXP i.MX RT: development platform for [PlatformIO](https://platformio.org)

[![Build Status](https://github.com/platformio/platform-nxpimxrt/workflows/Examples/badge.svg)](https://github.com/platformio/platform-nxpimxrt/actions)

The i.MX RT series of crossover processors features the Arm Cortex-M core, real-time functionality and MCU usability at a cost-effective price. Combining high performance with real-time functionality, the i.MX RT series of crossover processors are designed to support next-generation IoT applications with a high level of integration and security balanced with MCU-level usability.

* [Home](https://registry.platformio.org/platforms/platformio/nxpimxrt) (home page in the PlatformIO Registry)
* [Documentation](https://docs.platformio.org/page/platforms/nxpimxrt.html) (advanced usage, packages, boards, frameworks, etc.)

# Usage

1. [Install PlatformIO](https://platformio.org)
2. Create PlatformIO project and configure a platform option in [platformio.ini](https://docs.platformio.org/page/projectconf.html) file:

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

Please navigate to [documentation](https://docs.platformio.org/page/platforms/nxpimxrt.html).
