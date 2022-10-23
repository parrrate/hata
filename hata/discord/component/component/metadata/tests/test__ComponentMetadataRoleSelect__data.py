import vampytest

from ..role_select import ComponentMetadataRoleSelect

from .test__ComponentMetadataRoleSelect__constructor import _check_is_all_attribute_set


def test__ComponentMetadataRoleSelect__from_data():
    """
    Tests whether ``ComponentMetadataRoleSelect.from_data`` works as intended.
    """
    custom_id = 'oriental'
    enabled = False
    max_values = 10
    min_values = 9
    placeholder = 'swing'
    
    data = {
        'custom_id': custom_id,
        'disabled': not enabled,
        'max_values': max_values,
        'min_values': min_values,
        'placeholder': placeholder,
    }
    
    component_metadata = ComponentMetadataRoleSelect.from_data(data)
    _check_is_all_attribute_set(component_metadata)
    vampytest.assert_eq(component_metadata.custom_id, custom_id)
    vampytest.assert_eq(component_metadata.enabled, enabled)
    vampytest.assert_eq(component_metadata.max_values, max_values)
    vampytest.assert_eq(component_metadata.min_values, min_values)
    vampytest.assert_eq(component_metadata.placeholder, placeholder)


def test__ComponentMetadataRoleSelect__to_data():
    """
    Tests whether ``ComponentMetadataRoleSelect.to_data`` works as intended.
    
    Case: include defaults.
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
    
    component_metadata = ComponentMetadataRoleSelect(keyword_parameters)
    
    vampytest.assert_eq(
        component_metadata.to_data(
            defaults = True,
        ),
        {
            'custom_id': custom_id,
            'disabled': not enabled,
            'max_values': max_values,
            'min_values': min_values,
            'placeholder': placeholder,
        },
    )
