import os

from SCons.Script import (
   COMMAND_LINE_TARGETS
)

Import("env")

env.Append(
    CCFLAGS=[
        "-Os",
        "-fno-common",
        "-Wall",
        "-ffunction-sections",
        "-fdata-sections",
        "-ffreestanding",
        "-fno-builtin",
        "-fmerge-constants",
        "-mcpu=cortex-m7",
        "-mfpu=fpv5-sp-d16",
        "-mfloat-abi=hard",
        "-mthumb",
        "-fstack-usage",
    ],

    CPPDEFINES=[
        "__USE_CMSIS",
        "__REDLIB__",
        "CPU_MIMXRT1064DVL6A",
        "CPU_MIMXRT1064DVL6A_cm7",
        "FSL_RTOS_BM",
        "SDK_OS_BAREMETAL",
        "CR_INTEGER_PRINTF",
        ("SDK_DEBUGCONSOLE", 0),
        ("PRINTF_FLOAT_ENABLE", 0),
        ("XIP_EXTERNAL_FLASH", 1),
        ("XIP_BOOT_HEADER_ENABLE", 1),
        ("SERIAL_PORT_TYPE_UART", 1),
        "__MCUXPRESSO"
    ],

    LINKFLAGS=[
        "-nostdlib",
        "-Wl,-Map=" + os.path.join("$BUILD_DIR", os.path.basename(
            env.subst("${PROJECT_DIR}.map"))),
        "-Wl,--gc-sections",
        "-Wl,--sort-section=alignment",
        "-mcpu=cortex-m7",
        "-mfpu=fpv5-sp-d16",
        "-mfloat-abi=hard",
        "-mthumb",
    ]
)

is_build_type_debug = (
    set(["debug", "sizedata"]) & set(COMMAND_LINE_TARGETS)
    or env.GetProjectOption("build_type") == "debug"
)

sdk_includes = (
    "board",
    "source",
    "drivers",
    "device",
    "CMSIS",
    "xip",
    "utilities",
    os.path.join("component", "serial_manager"),
    os.path.join("component", "lists"),
    os.path.join("component", "uart")
)

env.Append(
    CPPPATH=[os.path.join("$PROJECT_SRC_DIR", inc) for inc in sdk_includes]
)
