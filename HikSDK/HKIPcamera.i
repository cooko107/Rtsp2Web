// HKIPcamera.i
/*  Example of wrapping a C function that takes a C double array as input using
 *  numpy typemaps for SWIG. */
%module HKIPcamera
%include <opencv/mat.i>
%cv_mat__instantiate_defaults
%header %{
    /*  Includes the header in the wrapper code */
    #include "HKIPcamera.h"
%}


%include "HKIPcamera.h"