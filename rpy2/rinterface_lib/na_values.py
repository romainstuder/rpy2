"""NA (Non-Available) values in R."""
import typing
from rpy2.rinterface_lib import _rinterface_capi as _rinterface
from rpy2.rinterface_lib import sexp

NA_Character = sexp.CharSexp(
    _rinterface.UninitializedRCapsule(sexp.RTYPES.CHARSXP.value)
)
NA_Integer: typing.Optional[sexp.NAIntegerType] = None
NA_Logical: typing.Optional[sexp.NALogicalType] = None
NA_Real: typing.Optional[sexp.NARealType] = None
NA_Complex: typing.Optional[sexp.NAComplexType] = None
