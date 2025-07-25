cmake_minimum_required(VERSION 3.22)

# Enable compile command to ease indexing with e.g. clangd
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# include(versioning.cmake)


#BEGIN firmware project configuration

#
# Core project settings
#
project(NUCLEO-G474-example)
enable_language(C ASM)

message("Build type: " ${CMAKE_BUILD_TYPE})

# Setup compiler settings
set(CMAKE_C_STANDARD                11)
set(CMAKE_C_STANDARD_REQUIRED       ON)
set(CMAKE_C_EXTENSIONS              ON)
set(PROJ_PATH                       ${CMAKE_CURRENT_SOURCE_DIR})
set(LIBRARY_PATH                    ${CMAKE_CURRENT_SOURCE_DIR}/library)
set(DRIVERS_PATH                    ${CMAKE_CURRENT_SOURCE_DIR}/Drivers)
set(MESSAGES_PATH                   ${CMAKE_CURRENT_SOURCE_DIR}/messages)
set(MESSAGES_GENERATED_PATH         ${MESSAGES_PATH}/generated)


include(${MESSAGES_PATH}/fetch_nanopb.cmake)

#
# Core MCU flags, CPU, instruction set and FPU setup
# Needs to be set properly for your MCU
#
set(CPU_PARAMETERS
    -mthumb
    -mcpu=cortex-m4
    -mfpu=fpv4-sp-d16
    -mfloat-abi=hard
    -fno-math-errno
    -fsingle-precision-constant
    -DARM_ARCH=4 # needed by QP
    -DSTM32G474xx
)

add_compile_options(
    ${CPU_PARAMETERS}
)

# Set linker script
set(linker_script_SRC               ${PROJ_PATH}/Core/bsp/device/stm32g474retx_flash.ld) 

set(EXECUTABLE                      ${CMAKE_PROJECT_NAME})

# include QPC
set(QPC_CFG_KERNEL qk)
set(QPC_CFG_GUI OFF)
set(QPC_CFG_UNIT_TEST OFF)
set(QPC_CFG_VERBOSE OFF)
set(QPC_CFG_PORT arm-cm)
add_subdirectory(${LIBRARY_PATH}/qpc/ test)




#
# List of source files to compile
#

set(messages_SRCS
${MESSAGES_GENERATED_PATH}/c/LogPrint.pb.c
${MESSAGES_GENERATED_PATH}/c/CLIData.pb.c
${MESSAGES_GENERATED_PATH}/c/AddXYToPlot.pb.c
${MESSAGES_GENERATED_PATH}/c/AddToBodePlot.pb.c
${MESSAGES_GENERATED_PATH}/c/ClearPlots.pb.c
${MESSAGES_GENERATED_PATH}/c/ConfigPlot.pb.c
${MESSAGES_GENERATED_PATH}/c/DrawBodePlot.pb.c
${MESSAGES_GENERATED_PATH}/c/DrawPlot.pb.c
${MESSAGES_GENERATED_PATH}/c/LogToPlot.pb.c
)

set(sources_SRCS 
    # processor startup
    ${PROJ_PATH}/Core/bsp/device/startup_stm32g474xx.s

    # cubeMX generated files
    ${PROJ_PATH}/Core/Src/stm32g4xx_it.c
    ${PROJ_PATH}/Core/Src/syscalls.c
    ${PROJ_PATH}/Core/Src/sysmem.c

    # application
    ${PROJ_PATH}/Core/Src/main.c
    ${PROJ_PATH}/Core/Src/interrupts.c

    # services
    ${PROJ_PATH}/Core/services/cli/cli_commands.c
    ${PROJ_PATH}/Core/services/cli/cli_manual_commands.c
    # ${PROJ_PATH}/Core/services/cli/cli.c
    ${PROJ_PATH}/Core/services/fault_manager.c
    ${PROJ_PATH}/Core/services/blinky.c  
    ${PROJ_PATH}/Core/services/director.c  
    ${PROJ_PATH}/Core/services/reset.c
    ${PROJ_PATH}/Core/services/reset_reason_print.c    
    ${PROJ_PATH}/Core/services/pc_com/hdlc.c
    ${PROJ_PATH}/Core/services/pc_com/crc16.c
    ${PROJ_PATH}/Core/services/pc_com/pc_com.c  

    # TODO: check if this file required
    ${PROJ_PATH}/Core/Src/system_stm32g4xx.c    
    ${PROJ_PATH}/Core/Src/stm32g4xx_hal_msp.c      

    # misc
    ${PROJ_PATH}/Core/Src/safe_strncpy.c
    
    # BSP
    ${PROJ_PATH}/Core/bsp/bsp.c
    ${PROJ_PATH}/Core/bsp/bsp_manual.c
    ${PROJ_PATH}/Core/bsp/gpio_stm32.c
    ${PROJ_PATH}/Core/bsp/uart.c
    ${PROJ_PATH}/Core/bsp/uart_mpu_specific.c
    ${PROJ_PATH}/Core/bsp/bsp_backup_ram.c



    # HAL
    ${DRIVERS_PATH}/STM32G4xx_HAL_Driver/Src/stm32g4xx_hal.c
    ${DRIVERS_PATH}/STM32G4xx_HAL_Driver/Src/stm32g4xx_hal_cortex.c
    ${DRIVERS_PATH}/STM32G4xx_HAL_Driver/Src/stm32g4xx_hal_gpio.c
    ${DRIVERS_PATH}/STM32G4xx_HAL_Driver/Src/stm32g4xx_hal_pcd.c
    ${DRIVERS_PATH}/STM32G4xx_HAL_Driver/Src/stm32g4xx_hal_pcd_ex.c
    
    ${DRIVERS_PATH}/STM32G4xx_HAL_Driver/Src/stm32g4xx_hal_pwr.c
    ${DRIVERS_PATH}/STM32G4xx_HAL_Driver/Src/stm32g4xx_hal_pwr_ex.c
    ${DRIVERS_PATH}/STM32G4xx_HAL_Driver/Src/stm32g4xx_hal_rcc.c
    ${DRIVERS_PATH}/STM32G4xx_HAL_Driver/Src/stm32g4xx_hal_rcc_ex.c
    ${DRIVERS_PATH}/STM32G4xx_HAL_Driver/Src/stm32g4xx_hal_tim.c
    ${DRIVERS_PATH}/STM32G4xx_HAL_Driver/Src/stm32g4xx_hal_fdcan.c
    ${DRIVERS_PATH}/STM32G4xx_HAL_Driver/Src/stm32g4xx_hal_tim_ex.c
    ${DRIVERS_PATH}/STM32G4xx_HAL_Driver/Src/stm32g4xx_hal_uart.c
    ${DRIVERS_PATH}/STM32G4xx_HAL_Driver/Src/stm32g4xx_ll_fmc.c
    ${DRIVERS_PATH}/STM32G4xx_HAL_Driver/Src/stm32g4xx_ll_usb.c
    ${DRIVERS_PATH}/STM32G4xx_HAL_Driver/Src/stm32g4xx_hal_adc.c
    ${DRIVERS_PATH}/STM32G4xx_HAL_Driver/Src/stm32g4xx_hal_adc_ex.c
    ${DRIVERS_PATH}/STM32G4xx_HAL_Driver/Src/stm32g4xx_hal_dma.c
    ${DRIVERS_PATH}/STM32G4xx_HAL_Driver/Src/stm32g4xx_hal_spi.c
    ${DRIVERS_PATH}/STM32G4xx_HAL_Driver/Src/stm32g4xx_hal_dac.c
    ${DRIVERS_PATH}/STM32G4xx_HAL_Driver/Src/stm32g4xx_hal_dac_ex.c
    ${DRIVERS_PATH}/STM32G4xx_HAL_Driver/Src/stm32g4xx_hal_uart_ex.c
    ${DRIVERS_PATH}/STM32G4xx_HAL_Driver/Src/stm32g4xx_hal_opamp.c
    


    # Segger RTT
    ${LIBRARY_PATH}/SEGGER_RTT_V810k/RTT/SEGGER_RTT.c
    ${LIBRARY_PATH}/SEGGER_RTT_V810k/RTT/SEGGER_RTT_printf.c

    # nanopb and messages
    ${nanopb_SRCS}
    ${messages_SRCS}

    # DMSIS DSP
    ${DRIVERS_PATH}/CMSIS/DSP/Source/ControllerFunctions/arm_pid_init_f32.c
)

#
# Include directories
#
set(include_path_DIRS
    ${PROJ_PATH}/Core/Src
    ${PROJ_PATH}/Core/Inc
    ${PROJ_PATH}/Core/bsp
    ${PROJ_PATH}/Core/services
    ${PROJ_PATH}/Core/services/cli
    ${PROJ_PATH}/Core/services/pc_com

    ${LIBRARY_PATH}/embedded-cli

    ${LIBRARY_PATH}/qpc/include
    ${LIBRARY_PATH}/qpc/ports/arm-cm/qk/config/
    ${LIBRARY_PATH}/qpc/ports/arm-cm/qk/gnu/
    
    ${LIBRARY_PATH}/tinyusb-0.17.0/src

    ${DRIVERS_PATH}/STM32G4xx_HAL_Driver/Inc
    ${DRIVERS_PATH}/STM32G4xx_HAL_Driver/Inc/Legacy 
       
    ${DRIVERS_PATH}/CMSIS/Device/ST/STM32G4xx/Include
    ${DRIVERS_PATH}/CMSIS/Include
    ${DRIVERS_PATH}/CMSIS/DSP/Include

    ${LIBRARY_PATH}/SEGGER_RTT_V810k/Config
    ${LIBRARY_PATH}/SEGGER_RTT_V810k/RTT 

    ${SHARED_PATH}/services
    ${SHARED_PATH}/bsp/interfaces
)

#
# Symbols definition
#
set(symbols_SYMB
    USE_HAL_DRIVER
    CFG_TUSB_MCU=OPT_MCU_STM32G4
)

# Executable files
add_executable(${EXECUTABLE} ${sources_SRCS})

# Include paths
target_include_directories(${EXECUTABLE} PRIVATE ${include_path_DIRS}
    ${MESSAGES_GENERATED_PATH}
    ${nanopb_SOURCE_DIR}
)

message(MESSAGES_GENERATED_PATH="${MESSAGES_GENERATED_PATH}")

# Project symbols
target_compile_definitions(${EXECUTABLE} PRIVATE ${symbols_SYMB})

# Configuration specific
add_compile_definitions(
  $<$<CONFIG:DEBUG>:DEBUG>
)

# Compiler options
target_compile_options(${EXECUTABLE} PRIVATE
    -Wall
    -Wextra
    # -Wpedantic
    -Wno-unused-parameter    
    $<$<COMPILE_LANGUAGE:ASM>:-x assembler-with-cpp -MMD -MP>
    $<$<CONFIG:DEBUG,RELEASE>: -O0 -g3>
)

# add the math library and qpc 
# linker throws undefined reference to `__errno' even though -lm and -c added, which should add m lib
target_link_libraries(${EXECUTABLE} PRIVATE m qpc)

# Linker options
target_link_options(${EXECUTABLE} PRIVATE
    -T${linker_script_SRC}
    ${CPU_PARAMETERS}
    -Wl,-Map=${CMAKE_PROJECT_NAME}.map
    --specs=nosys.specs
    -u _printf_float  # STDIO float formatting support
    -Wl,--start-group
    -lc
    -lm
    -Wl,--end-group
    -Wl,--print-memory-usage
)

# Execute post-build to print size
add_custom_command(TARGET ${EXECUTABLE} POST_BUILD
    COMMAND ${CMAKE_SIZE} $<TARGET_FILE:${EXECUTABLE}>
)

# Convert output to hex and binary
add_custom_command(TARGET ${EXECUTABLE} POST_BUILD
    COMMAND ${CMAKE_OBJCOPY} -O ihex $<TARGET_FILE:${EXECUTABLE}> ${EXECUTABLE}.hex
)

# Convert to bin file -> add conditional check?
add_custom_command(TARGET ${EXECUTABLE} POST_BUILD
    COMMAND ${CMAKE_OBJCOPY} -O binary $<TARGET_FILE:${EXECUTABLE}> ${EXECUTABLE}.bin
)