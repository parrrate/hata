import vampytest

from ..mentionable_select import ComponentMetadataMentionableSelect


def _check_is_all_attribute_set(component_metadata):
    """
    Checks whether the ``ComponentMetadataMentionableSelect`` has all it's attributes set.
    """
    vampytest.assert_instance(component_metadata, ComponentMetadataMentionableSelect)
    vampytest.assert_instance(component_metadata.custom_id, str, nullable = True)
    vampytest.assert_instance(component_metadata.enabled, bool)
    vampytest.assert_instance(component_metadata.max_values, int)
    vampytest.assert_instance(component_metadata.min_values, int)
    vampytest.assert_instance(component_metadata.placeholder, str, nullable = True)



def test__ComponentMetadataMentionableSelect__new__0():
    """
    Tests whether ``ComponentMetadataMentionableSelect.__new__`` works as intended.
    
    Case: no fields given.
    """
    keyword_parameters = {}
    
    component_metadata = ComponentMetadataMentionableSelect(keyword_parameters)
    _check_is_all_attribute_set(component_metadata)


def test__ComponentMetadataMentionableSelect__new__1():
    """
    Tests whether ``ComponentMetadataMentionableSelect.__new__`` works as intended.
    
    Case: all fields given
    """
    custom_id = 'oriental'
    enabled = False
    max_values = 10
    min_values = 9
    placeholder = 'swing'
    
    keyword_parameters = {
        'custom_id': custom_id,
        'enabled': enabled,
        'max_values': max_values,
        'min_values': min_values,
        'placeholder': placeholder,
    }
    
    component_metadata = ComponentMetadataMentionableSelect(keyword_parameters)
    _check_is_all_attribute_set(component_metadata)
    vampytest.assert_eq(component_metadata.custom_id, custom_id)
    vampytest.assert_eq(component_metadata.enabled, enabled)
    vampytest.assert_eq(component_metadata.max_values, max_values)
    vampytest.assert_eq(component_metadata.min_values, min_values)
    vampytest.assert_eq(component_metadata.placeholder, placeholder)
