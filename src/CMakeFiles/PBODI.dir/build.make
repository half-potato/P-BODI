# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.4

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/Cellar/cmake/3.4.1/bin/cmake

# The command to remove a file.
RM = /usr/local/Cellar/cmake/3.4.1/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/amai/PBODI

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/amai/PBODI/src

# Include any dependencies generated for this target.
include CMakeFiles/PBODI.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/PBODI.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/PBODI.dir/flags.make

CMakeFiles/PBODI.dir/main.cpp.o: CMakeFiles/PBODI.dir/flags.make
CMakeFiles/PBODI.dir/main.cpp.o: main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/amai/PBODI/src/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/PBODI.dir/main.cpp.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/PBODI.dir/main.cpp.o -c /Users/amai/PBODI/src/main.cpp

CMakeFiles/PBODI.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/PBODI.dir/main.cpp.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/amai/PBODI/src/main.cpp > CMakeFiles/PBODI.dir/main.cpp.i

CMakeFiles/PBODI.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/PBODI.dir/main.cpp.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/amai/PBODI/src/main.cpp -o CMakeFiles/PBODI.dir/main.cpp.s

CMakeFiles/PBODI.dir/main.cpp.o.requires:

.PHONY : CMakeFiles/PBODI.dir/main.cpp.o.requires

CMakeFiles/PBODI.dir/main.cpp.o.provides: CMakeFiles/PBODI.dir/main.cpp.o.requires
	$(MAKE) -f CMakeFiles/PBODI.dir/build.make CMakeFiles/PBODI.dir/main.cpp.o.provides.build
.PHONY : CMakeFiles/PBODI.dir/main.cpp.o.provides

CMakeFiles/PBODI.dir/main.cpp.o.provides.build: CMakeFiles/PBODI.dir/main.cpp.o


CMakeFiles/PBODI.dir/Perspective.cpp.o: CMakeFiles/PBODI.dir/flags.make
CMakeFiles/PBODI.dir/Perspective.cpp.o: Perspective.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/amai/PBODI/src/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/PBODI.dir/Perspective.cpp.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/PBODI.dir/Perspective.cpp.o -c /Users/amai/PBODI/src/Perspective.cpp

CMakeFiles/PBODI.dir/Perspective.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/PBODI.dir/Perspective.cpp.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/amai/PBODI/src/Perspective.cpp > CMakeFiles/PBODI.dir/Perspective.cpp.i

CMakeFiles/PBODI.dir/Perspective.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/PBODI.dir/Perspective.cpp.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/amai/PBODI/src/Perspective.cpp -o CMakeFiles/PBODI.dir/Perspective.cpp.s

CMakeFiles/PBODI.dir/Perspective.cpp.o.requires:

.PHONY : CMakeFiles/PBODI.dir/Perspective.cpp.o.requires

CMakeFiles/PBODI.dir/Perspective.cpp.o.provides: CMakeFiles/PBODI.dir/Perspective.cpp.o.requires
	$(MAKE) -f CMakeFiles/PBODI.dir/build.make CMakeFiles/PBODI.dir/Perspective.cpp.o.provides.build
.PHONY : CMakeFiles/PBODI.dir/Perspective.cpp.o.provides

CMakeFiles/PBODI.dir/Perspective.cpp.o.provides.build: CMakeFiles/PBODI.dir/Perspective.cpp.o


# Object files for target PBODI
PBODI_OBJECTS = \
"CMakeFiles/PBODI.dir/main.cpp.o" \
"CMakeFiles/PBODI.dir/Perspective.cpp.o"

# External object files for target PBODI
PBODI_EXTERNAL_OBJECTS =

PBODI: CMakeFiles/PBODI.dir/main.cpp.o
PBODI: CMakeFiles/PBODI.dir/Perspective.cpp.o
PBODI: CMakeFiles/PBODI.dir/build.make
PBODI: /usr/local/lib/libopencv_videostab.2.4.12.dylib
PBODI: /usr/local/lib/libopencv_ts.a
PBODI: /usr/local/lib/libopencv_superres.2.4.12.dylib
PBODI: /usr/local/lib/libopencv_stitching.2.4.12.dylib
PBODI: /usr/local/lib/libopencv_contrib.2.4.12.dylib
PBODI: /usr/local/lib/libopencv_nonfree.2.4.12.dylib
PBODI: /usr/local/lib/libopencv_ocl.2.4.12.dylib
PBODI: /usr/local/lib/libopencv_gpu.2.4.12.dylib
PBODI: /usr/local/lib/libopencv_photo.2.4.12.dylib
PBODI: /usr/local/lib/libopencv_objdetect.2.4.12.dylib
PBODI: /usr/local/lib/libopencv_legacy.2.4.12.dylib
PBODI: /usr/local/lib/libopencv_video.2.4.12.dylib
PBODI: /usr/local/lib/libopencv_ml.2.4.12.dylib
PBODI: /usr/local/lib/libopencv_calib3d.2.4.12.dylib
PBODI: /usr/local/lib/libopencv_features2d.2.4.12.dylib
PBODI: /usr/local/lib/libopencv_highgui.2.4.12.dylib
PBODI: /usr/local/lib/libopencv_imgproc.2.4.12.dylib
PBODI: /usr/local/lib/libopencv_flann.2.4.12.dylib
PBODI: /usr/local/lib/libopencv_core.2.4.12.dylib
PBODI: CMakeFiles/PBODI.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/amai/PBODI/src/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable PBODI"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/PBODI.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/PBODI.dir/build: PBODI

.PHONY : CMakeFiles/PBODI.dir/build

CMakeFiles/PBODI.dir/requires: CMakeFiles/PBODI.dir/main.cpp.o.requires
CMakeFiles/PBODI.dir/requires: CMakeFiles/PBODI.dir/Perspective.cpp.o.requires

.PHONY : CMakeFiles/PBODI.dir/requires

CMakeFiles/PBODI.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/PBODI.dir/cmake_clean.cmake
.PHONY : CMakeFiles/PBODI.dir/clean

CMakeFiles/PBODI.dir/depend:
	cd /Users/amai/PBODI/src && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/amai/PBODI /Users/amai/PBODI /Users/amai/PBODI/src /Users/amai/PBODI/src /Users/amai/PBODI/src/CMakeFiles/PBODI.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/PBODI.dir/depend
