import vampytest

from ..invitable import put_invitable_into


def test__put_invitable_into():
    """
    Tests whether ``put_invitable_into`` is working as intended.
    """
    for input_, defaults, expected_output in (
        (True, False, {}),
        (False, False, {'thread_metadata': {'invitable': False}}),
        (True, True, {'thread_metadata': {'invitable': True}}),
    ):
        data = put_invitable_into(input_, {}, defaults)
        vampytest.assert_eq(data, expected_output)
