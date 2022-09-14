import vampytest


from ..applied_tag_ids import put_applied_tag_ids_into


def test__put_applied_tag_ids_into():
    """
    Tests whether ``put_applied_tag_ids_into`` is working as intended.
    """
    applied_tag_id = 202209140023
    
    for input_, defaults, expected_output in (
        (None, False, {}),
        (None, True, {'applied_tags': []}),
        ((applied_tag_id, ), False, {'applied_tags': [str(applied_tag_id)]}),
    ):
        data = put_applied_tag_ids_into(input_, {}, defaults)
        vampytest.assert_eq(data, expected_output)
