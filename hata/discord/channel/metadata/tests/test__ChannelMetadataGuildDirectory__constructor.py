import vampytest

from ....permission import PermissionOverwrite, PermissionOverwriteTargetType

from .. import ChannelMetadataGuildDirectory


def assert_fields_set(channel_metadata):
    vampytest.assert_instance(channel_metadata.parent_id, int)
    vampytest.assert_instance(channel_metadata.name, str)
    vampytest.assert_instance(channel_metadata._permission_cache, dict, nullable = True)
    vampytest.assert_instance(channel_metadata.permission_overwrites, dict, nullable = True)
    vampytest.assert_instance(channel_metadata.position, int)


def test__ChannelMetadataGuildDirectory__new__0():
    """
    Tests whether ``ChannelMetadataGuildDirectory.__new__`` works as intended.
    
    Case: all fields given.
    """
    parent_id = 202209170071
    name = 'Armelyrics'
    permission_overwrites = [
        PermissionOverwrite(202209170051, target_type = PermissionOverwriteTargetType.user)
    ]
    position = 7
    
    keyword_parameters = {
        'parent_id': parent_id,
        'name': name,
        'permission_overwrites': permission_overwrites,
        'position': position,
    }
    channel_metadata = ChannelMetadataGuildDirectory(keyword_parameters)
    
    vampytest.assert_instance(channel_metadata, ChannelMetadataGuildDirectory)
    vampytest.assert_eq(keyword_parameters, {})
    assert_fields_set(channel_metadata)
    
    vampytest.assert_eq(channel_metadata.parent_id, parent_id)
    vampytest.assert_eq(channel_metadata.name, name)
    vampytest.assert_eq(
        channel_metadata.permission_overwrites,
        {permission_overwrite.target_id: permission_overwrite for permission_overwrite in permission_overwrites},
    )
    vampytest.assert_eq(channel_metadata.position, position)


def test__ChannelMetadataGuildDirectory__new__1():
    """
    Tests whether ``ChannelMetadataGuildDirectory.__new__`` works as intended.
    
    Case: no fields given.
    """
    keyword_parameters = {}
    
    channel_metadata = ChannelMetadataGuildDirectory(keyword_parameters)
    
    vampytest.assert_instance(channel_metadata, ChannelMetadataGuildDirectory)
    vampytest.assert_eq(keyword_parameters, {})
    assert_fields_set(channel_metadata)


def test__ChannelMetadataGuildDirectory__create_empty():
    """
    Tests whether ``ChannelMetadataGuildDirectory._create_empty`` works as intended.
    """
    channel_metadata = ChannelMetadataGuildDirectory._create_empty()
    
    vampytest.assert_instance(channel_metadata, ChannelMetadataGuildDirectory)
    assert_fields_set(channel_metadata)



def test__ChannelMetadataGuildDirectory__precreate__0():
    """
    Tests whether ``ChannelMetadataGuildDirectory.precreate`` works as intended.
    
    Case: all fields given.
    """
    parent_id = 202209170052
    name = 'Armelyrics'
    permission_overwrites = [
        PermissionOverwrite(202209170053, target_type = PermissionOverwriteTargetType.user)
    ]
    position = 7
    
    keyword_parameters = {
        'parent_id': parent_id,
        'name': name,
        'permission_overwrites': permission_overwrites,
        'position': position,
    }
    
    channel_metadata = ChannelMetadataGuildDirectory.precreate(keyword_parameters)
    
    vampytest.assert_instance(channel_metadata, ChannelMetadataGuildDirectory)
    vampytest.assert_eq(keyword_parameters, {})
    assert_fields_set(channel_metadata)
    
    vampytest.assert_eq(channel_metadata.parent_id, parent_id)
    vampytest.assert_eq(channel_metadata.name, name)
    vampytest.assert_eq(
        channel_metadata.permission_overwrites,
        {permission_overwrite.target_id: permission_overwrite for permission_overwrite in permission_overwrites},
    )
    vampytest.assert_eq(channel_metadata.position, position)


def test__ChannelMetadataGuildDirectory__precreate__1():
    """
    Tests whether ``ChannelMetadataGuildDirectory.precreate`` works as intended.
    
    Case: no fields given.
    """
    keyword_parameters = {}
    
    channel_metadata = ChannelMetadataGuildDirectory.precreate(keyword_parameters)
    
    vampytest.assert_instance(channel_metadata, ChannelMetadataGuildDirectory)
    vampytest.assert_eq(keyword_parameters, {})
    assert_fields_set(channel_metadata)
