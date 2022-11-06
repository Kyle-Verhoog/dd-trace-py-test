#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "libddwaf_static" for configuration "Release"
set_property(TARGET libddwaf_static APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(libddwaf_static PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libddwaf.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS libddwaf_static )
list(APPEND _IMPORT_CHECK_FILES_FOR_libddwaf_static "${_IMPORT_PREFIX}/lib/libddwaf.a" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
