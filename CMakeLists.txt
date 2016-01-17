cmake_minimum_required(VERSION 2.8)
project( PBODI )
find_package( OpenCV REQUIRED )
include_directories( 
	${OpenCV_INCLUDE_DIRS}
	${CMAKE_CURRENT_SOURCE_DIR}/src
)
add_executable( PBODI src/main.cpp src/Perspective.cpp)
set_property(PBODY tgt PROPERTY CXX_STANDARD_REQUIRED 11)
target_link_libraries(PBODI ${OpenCV_LIBS} )
