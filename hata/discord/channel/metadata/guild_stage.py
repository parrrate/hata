__all__ = ('ChannelMetadataGuildStage',)


from scarletio import copy_docs

from ...permission import Permission
from ...permission.permission import (
    PERMISSION_MASK_CONNECT, PERMISSION_MASK_VIEW_CHANNEL, PERMISSION_NONE, PERMISSION_TEXT_DENY,
    PERMISSION_VOICE_DENY_CONNECTION
)
from ...preconverters import preconvert_str

from ..fields.topic import parse_topic, put_topic_into, validate_topic

from .guild_main_base import ChannelMetadataGuildMainBase
from .guild_voice_base import ChannelMetadataGuildVoiceBase


class ChannelMetadataGuildStage(ChannelMetadataGuildVoiceBase):
    """
    Guild voice channel metadata.
    
    Attributes
    ----------
    _permission_cache : `None`, `dict` of (`int`, ``Permission``) items
        A `user_id` to ``Permission`` relation mapping for caching permissions. Defaults to `None`.
    parent_id : `int`
        The channel's parent's identifier.
    name : `str`
        The channel's name.
    permission_overwrites : `dict` of (`int`, ``PermissionOverwrite``) items
        The channel's permission overwrites.
    position : `int`
        The channel's position.
    bitrate : `int`
        The bitrate (in bits) of the voice channel.
    region : `None`, ``VoiceRegion``
        The voice region of the channel.
    user_limit : `int`
        The maximal amount of users, who can join the voice channel, or `0` if unlimited.
    topic : `None`, `str`
        The channel's topic.
    
    Class Attributes
    ----------------
    order_group: `int` = `2`
        The channel's order group used when sorting channels.
    """
    __slots__ = ('topic',)

    @copy_docs(ChannelMetadataGuildVoiceBase._is_equal_same_type)
    def _is_equal_same_type(self, other):
        if not ChannelMetadataGuildVoiceBase._is_equal_same_type(self, other):
            return False
        
        # topic
        if self.topic != other.topic:
            return False
        
        return True
    
    
    @classmethod
    @copy_docs(ChannelMetadataGuildVoiceBase._create_empty)
    def _create_empty(cls):
        self = super(ChannelMetadataGuildStage, cls)._create_empty()
        
        self.topic = None
        
        return self
    
    
    @copy_docs(ChannelMetadataGuildVoiceBase._update_attributes)
    def _update_attributes(self, data):
        ChannelMetadataGuildVoiceBase._update_attributes(self, data)
        
        # topic
        self.topic = parse_topic(data)
    
    
    @copy_docs(ChannelMetadataGuildVoiceBase._difference_update_attributes)
    def _difference_update_attributes(self, data):
        old_attributes = ChannelMetadataGuildVoiceBase._difference_update_attributes(self, data)
        
        # topic
        topic = parse_topic(data)
        if self.topic != topic:
            old_attributes['topic'] = self.topic
            self.topic = topic
        
        return old_attributes
    
    
    @classmethod
    @copy_docs(ChannelMetadataGuildVoiceBase._precreate)
    def _precreate(cls, keyword_parameters):
        self = super(ChannelMetadataGuildStage, cls)._precreate(keyword_parameters)
        
        # topic
        try:
            topic = keyword_parameters.pop('topic')
        except KeyError:
            pass
        else:
            self.topic = validate_topic(topic)
        
        return self
    
    
    @copy_docs(ChannelMetadataGuildVoiceBase._to_data)
    def _to_data(self):
        data = ChannelMetadataGuildVoiceBase._to_data(self)
        
        # topic
        put_topic_into(self.topic, data, True)
        
        return data
    
    
    @copy_docs(ChannelMetadataGuildMainBase._get_permissions_for)
    def _get_permissions_for(self, channel_entity, user):
        result = self._get_base_permissions_for(channel_entity, user)
        if not result & PERMISSION_MASK_VIEW_CHANNEL:
            return PERMISSION_NONE
        
        # voice channels don't have text permissions
        result &= PERMISSION_TEXT_DENY
        
        if not result & PERMISSION_MASK_CONNECT:
            result &= PERMISSION_VOICE_DENY_CONNECTION
        
        return Permission(result)
    
    
    @copy_docs(ChannelMetadataGuildMainBase._get_permissions_for_roles)
    def _get_permissions_for_roles(self, channel_entity, roles):
        result = self._get_base_permissions_for_roles(channel_entity, roles)
        if not result & PERMISSION_MASK_VIEW_CHANNEL:
            return PERMISSION_NONE
        
        # voice channels don't have text permissions
        result &= PERMISSION_TEXT_DENY
        
        if not result & PERMISSION_MASK_CONNECT:
            result &= PERMISSION_VOICE_DENY_CONNECTION
        
        return Permission(result)
