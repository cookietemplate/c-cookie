cmake_minimum_required(VERSION {{cookiecutter.cmake_minimum_required}})
project({{cookiecutter.project_slug}} C)
include(CTest)

# C standard
set(CMAKE_C_STANDARD {{cookiecutter.c_standard}})

# Output paths
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)
set(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR}/lib)

# Header files
include_directories("${PROJECT_SOURCE_DIR}/{{'include' if cookiecutter.has_include_folder else 'src'}}")

# Project source files
add_subdirectory(src)

{% if cookiecutter.has_example -%}
# Examples
option(BUILD_EXAMPLES "Build examples" ON)
if(BUILD_EXAMPLES)
    message(STATUS "Building examples")
    add_subdirectory(example)
endif()
{% endif -%}

{% if cookiecutter.has_test -%}
# Tests
option(BUILD_TESTING "Enable testing" ON)
if(BUILD_TESTING)
    message(STATUS "Building tests")
    enable_testing()
    add_subdirectory(test)
endif()
{% endif -%}
