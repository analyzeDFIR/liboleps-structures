## -*- coding: UTF-8 -*_
## oleps.py
##
## Copyright (c) 2018 analyzeDFIR
## 
## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the "Software"), to deal
## in the Software without restriction, including without limitation the rights
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
## copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:
## 
## The above copyright notice and this permission notice shall be included in all
## copies or substantial portions of the Software.
## 
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
## SOFTWARE.

from construct import *

OLETypedPropertyValueTypes = Enum(Int16ul,
    VT_EMPTY            = 0x00,
    VT_NULL	        = 0x01,
    VT_I2	        = 0x02,
    VT_I4	        = 0x03,
    VT_R4	        = 0x04,
    VT_R8	        = 0x05,
    VT_CY	        = 0x06,
    VT_DATE	        = 0x07,
    VT_BSTR	        = 0x08,
    VT_ERROR	        = 0x0A,
    VT_BOOL	        = 0x0B,
    VT_DECIMAL	        = 0x0E,
    VT_I1	        = 0x10,
    VT_UI1	        = 0x11,
    VT_UI2	        = 0x12,
    VT_UI4	        = 0x13,
    VT_I8	        = 0x14,
    VT_UI8	        = 0x15,
    VT_INT	        = 0x16,
    VT_UINT	        = 0x17,
    VT_LPSTR	        = 0x1E,
    VT_LPWSTR	        = 0x1F,
    VT_FILETIME	        = 0x40,
    VT_BLOB	        = 0x41,
    VT_STREAM	        = 0x42,
    VT_STORAGE	        = 0x43,
    VT_STREAMED_OBJECT  = 0x0044,
    VT_STORED_OBJECT    = 0x0045,
    VT_BLOB_OBJECT      = 0x0046,
    VT_CF               = 0x0047,
    VT_CLSID            = 0x0048,
    VT_VERSIONED_STREAM = 0x0049,
    VT_VECTOR_I2	= 0x1002,
    VT_VECTOR_I4	= 0x1003,
    VT_VECTOR_R4	= 0x1004,
    VT_VECTOR_R8	= 0x1005,
    VT_VECTOR_CY	= 0x1006,
    VT_VECTOR_DATE	= 0x1007,
    VT_VECTOR_BSTR	= 0x1008,
    VT_VECTOR_ERROR	= 0x100A,
    VT_VECTOR_BOOL	= 0x100B,
    VT_VECTOR_VARIANT	= 0x100C,
    VT_VECTOR_I1	= 0x1010,
    VT_VECTOR_UI1	= 0x1011,
    VT_VECTOR_UI2	= 0x1012,
    VT_VECTOR_UI4	= 0x1013,
    VT_VECTOR_I8	= 0x1014,
    VT_VECTOR_UI8	= 0x1015,
    VT_VECTOR_LPSTR	= 0x101E,
    VT_VECTOR_LPWSTR	= 0x101F,
    VT_VECTOR_FILETIME	= 0x1040,
    VT_VECTOR_CF	= 0x1047,
    VT_VECTOR_CLSID	= 0x1048,
    VT_ARRAY_I2	        = 0x2002,
    VT_ARRAY_I4	        = 0x2003,
    VT_ARRAY_R4	        = 0x2004,
    VT_ARRAY_R8	        = 0x2005,
    VT_ARRAY_CY	        = 0x2006,
    VT_ARRAY_DATE	= 0x2007,
    VT_ARRAY_BSTR	= 0x2008,
    VT_ARRAY_ERROR	= 0x200A,
    VT_ARRAY_BOOL	= 0x200B,
    VT_ARRAY_VARIANT	= 0x200C,
    VT_ARRAY_DECIMAL	= 0x200E,
    VT_ARRAY_I1	        = 0x2010,
    VT_ARRAY_UI1	= 0x2011,
    VT_ARRAY_UI2	= 0x2012,
    VT_ARRAY_UI4	= 0x2013,
    VT_ARRAY_INT	= 0x2016,
    VT_ARRAY_UINT	= 0x2017
)
