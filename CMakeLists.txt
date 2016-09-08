cmake_minimum_required(VERSION 3.6)
project(libfixmatrix)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
set(CMAKE_DEBUG_POSTFIX d)

SET(CMAKE_ARCHIVE_OUTPUT_DIRECTORY         ${CMAKE_CURRENT_BINARY_DIR}/lib)
SET(CMAKE_ARCHIVE_OUTPUT_DIRECTORY_RELEASE ${CMAKE_ARCHIVE_OUTPUT_DIRECTORY})
SET(CMAKE_ARCHIVE_OUTPUT_DIRECTORY_DEBUG   ${CMAKE_ARCHIVE_OUTPUT_DIRECTORY})

set(SOURCES ${CMAKE_CURRENT_SOURCE_DIR}/libfixmatrix)
set(SOURCE_FILES
    ${SOURCES}/fixarray.c
    ${SOURCES}/fixmatrix.c
    ${SOURCES}/fixquat.c
    ${SOURCES}/fixstring.c
    ${SOURCES}/fixvector2d.c
    ${SOURCES}/fixvector3d.c)

set(HEADER_FILES
    ${SOURCES}/fixarray.h
    ${SOURCES}/fixmatrix.h
    ${SOURCES}/fixquat.h
    ${SOURCES}/fixstring.h
    ${SOURCES}/fixvector2d.h
    ${SOURCES}/fixvector3d.h)

add_library(libfixmatrix STATIC ${HEADER_FILES} ${SOURCE_FILES})
target_link_libraries(libfixmatrix ${CONAN_LIBS})