import vampytest

from ..helpers import serializable_localized_dictionary_builder
from ..preinstanced import Locale


def _iter_options__passing():
    yield (
        None,
        'cart',
        None,
    )
    
    yield (
        [],
        'cart',
        None,
    )
    
    yield (
        [(Locale.greek.value, 'miau')],
        'cart',
        {Locale.greek.value: 'miau'},
    )
    
    yield (
        [(Locale.greek, 'miau')],
        'cart',
        {Locale.greek.value: 'miau'},
    )
    
    yield (
        {},
        'cart',
        None,
    )
    
    yield (
        {Locale.greek.value: 'miau'},
        'cart',
        {Locale.greek.value: 'miau'},
    )
    
    yield (
        {Locale.greek: 'miau'},
        'cart',
        {Locale.greek.value: 'miau'},
    )


def _iter_options__type_error():
    yield (
        12.6,
        'cart',
    )


def _iter_options__value_error():
    yield (
        [(Locale.greek, 'miau', 'HUH')],
        'cart',
    )


@vampytest._(vampytest.call_from(_iter_options__passing()).returning_last())
@vampytest._(vampytest.call_from(_iter_options__type_error()).raising(TypeError))
@vampytest._(vampytest.call_from(_iter_options__value_error()).raising(ValueError))
def test__serializable_localized_dictionary_builder(dictionary, parameter_name):
    """
    Tests whether ``serializable_localized_dictionary_builder`` works as intended.
    
    Parameters
    ----------
    dictionary : `None | dict<Locale | str, str> | (set | tuple | list)<(Locale | str, str)>`
        The value to convert to json serializable localized dictionary.
    
    parameter_name : `str`
        The parameter's name to raise exception with.
    
    Returns
    -------
    output : `None | dict<str, str>`
    
    Raises
    ------
    TypeError
    ValueError
    """
    output = serializable_localized_dictionary_builder(dictionary, parameter_name)
    
    vampytest.assert_instance(output, dict, nullable = True)
    
    if (output is not None):
        for key, value in output.items():
            vampytest.assert_instance(key, str)
            vampytest.assert_instance(value, str)
    
    return output
