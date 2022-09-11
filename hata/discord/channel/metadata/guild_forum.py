__all__ = ('ChannelMetadataGuildForum',)


from scarletio import copy_docs

from ...emoji import Emoji, put_exclusive_emoji_data_into
from ...permission import Permission
from ...permission.permission import PERMISSION_MASK_VIEW_CHANNEL, PERMISSION_NONE, PERMISSION_THREAD_AND_VOICE_DENY
from ...preconverters import preconvert_flag, preconvert_int, preconvert_int_options, preconvert_str

from ..constants import AUTO_ARCHIVE_DEFAULT, AUTO_ARCHIVE_OPTIONS
from ..fields.available_tags import parse_available_tags, validate_available_tags
from ..fields.default_thread_auto_archive_after import parse_default_thread_auto_archive_after
from ..fields.default_thread_reaction import parse_default_thread_reaction
from ..fields.default_thread_slowmode import parse_default_thread_slowmode
from ..fields.flags import parse_flags
from ..fields.topic import parse_topic
from ..flags import ChannelFlag

from .guild_main_base import ChannelMetadataGuildMainBase


class ChannelMetadataGuildForum(ChannelMetadataGuildMainBase):
    """
    Guild forum channel metadata.
    
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
    available_tags : `None`, `tuple` of ``ForumTag``
        The available tags to assign to the child-thread channels.
    default_thread_auto_archive_after : `int`
        The default duration (in seconds) for newly created threads to automatically archive the themselves. Defaults
        to `3600`. Can be one of: `3600`, `86400`, `259200`, `604800`.
    default_thread_reaction : `None`, ``Emoji``
        The emoji to show in the add reaction button on a thread of the forum channel.
    default_thread_slowmode : `int`
        The default slowmode applied to the channel's threads.
    flags : ``ChannelFlag``
        The channel's flags.
    topic : `None`, `str`
        The channel's topic.
    
    Class Attributes
    ----------------
    order_group: `int` = `0`
        The channel's order group used when sorting channels.
    """
    __slots__ = (
        'available_tags', 'default_thread_auto_archive_after','default_thread_reaction', 'default_thread_slowmode', 
        'flags', 'topic',
    )
    
    @copy_docs(ChannelMetadataGuildMainBase._is_equal_same_type)
    def _is_equal_same_type(self, other):
        if not ChannelMetadataGuildMainBase._is_equal_same_type(self, other):
            return False
        
        # available_tags
        if self.available_tags != other.available_tags:
            return False
        
        # default_thread_auto_archive_after
        if self.default_thread_auto_archive_after != other.default_thread_auto_archive_after:
            return False
        
        # default_thread_reaction
        if self.default_thread_reaction != other.default_thread_reaction:
            return False
        
        # default_thread_slowmode
        if self.default_thread_slowmode != other.default_thread_slowmode:
            return False
        
        # flags
        if self.flags != other.flags:
            return False
        
        # topic
        if self.topic != other.topic:
            return False
        
        return True
    
    
    @copy_docs(ChannelMetadataGuildMainBase._get_display_name)
    def _get_display_name(self):
        return self.name.upper()
    
    
    @classmethod
    @copy_docs(ChannelMetadataGuildMainBase._create_empty)
    def _create_empty(cls):
        self = super(ChannelMetadataGuildForum, cls)._create_empty()
        
        self.available_tags = None
        self.default_thread_auto_archive_after = AUTO_ARCHIVE_DEFAULT
        self.default_thread_reaction = None
        self.default_thread_slowmode = 0
        self.flags = ChannelFlag()
        self.topic = None
        
        return self
    
    
    @copy_docs(ChannelMetadataGuildMainBase._update_attributes)
    def _update_attributes(self, data):
        ChannelMetadataGuildMainBase._update_attributes(self, data)
        
        # available_tags
        self.available_tags = parse_available_tags(data)
        
        # default_thread_auto_archive_after
        self.default_thread_auto_archive_after = parse_default_thread_auto_archive_after(data)
        
        # default_thread_reaction
        self.default_thread_reaction = parse_default_thread_reaction(data)
        
        # default_thread_slowmode
        self.default_thread_slowmode = parse_default_thread_slowmode(data)
        
        # flags
        self.flags = parse_flags(data)
        
        # topic
        self.topic = parse_topic(data)
    
    
    @copy_docs(ChannelMetadataGuildMainBase._difference_update_attributes)
    def _difference_update_attributes(self, data):
        old_attributes = ChannelMetadataGuildMainBase._difference_update_attributes(self, data)
        
        # available_tags
        available_tags = parse_available_tags(data)
        if (self.available_tags != available_tags):
            old_attributes['available_tags'] = self.available_tags
            self.available_tags = available_tags
        
        # default_thread_auto_archive_after
        default_thread_auto_archive_after = parse_default_thread_auto_archive_after(data)
        if self.default_thread_auto_archive_after != default_thread_auto_archive_after:
            old_attributes['default_thread_auto_archive_after'] = self.default_thread_auto_archive_after
            self.default_thread_auto_archive_after = default_thread_auto_archive_after
        
        # default_thread_reaction
        default_thread_reaction = parse_default_thread_reaction(data)
        if self.default_thread_reaction != default_thread_reaction:
            old_attributes['default_thread_reaction'] = self.default_thread_reaction
            self.default_thread_reaction = default_thread_reaction
        
        # default_thread_slowmode
        default_thread_slowmode = parse_default_thread_slowmode(data)
        if self.default_thread_slowmode != default_thread_slowmode:
            old_attributes['default_thread_slowmode'] = self.default_thread_slowmode
            self.default_thread_slowmode = default_thread_slowmode
        
        # flags
        flags = parse_flags(data)
        if (self.flags != flags):
            old_attributes['flags'] = self.flags
            self.flags = flags
        
        # topic
        topic = parse_topic(data)
        if self.topic != topic:
            old_attributes['topic'] = self.topic
            self.topic = topic
        
        return old_attributes
    
    
    @copy_docs(ChannelMetadataGuildMainBase._get_permissions_for)
    def _get_permissions_for(self, channel_entity, user):
        result = self._get_base_permissions_for(channel_entity, user)
        if not result & PERMISSION_MASK_VIEW_CHANNEL:
            return PERMISSION_NONE
        
        # forum channels do not have thread and voice related permissions
        result &= PERMISSION_THREAD_AND_VOICE_DENY
        
        return Permission(result)
    
    
    @copy_docs(ChannelMetadataGuildMainBase._get_permissions_for_roles)
    def _get_permissions_for_roles(self, channel_entity, roles):
        result = self._get_base_permissions_for_roles(channel_entity, roles)
        if not result & PERMISSION_MASK_VIEW_CHANNEL:
            return PERMISSION_NONE
        
        # forum channels do not have thread and voice related permissions
        result &= PERMISSION_THREAD_AND_VOICE_DENY
        return Permission(result)
    
    
    @classmethod
    @copy_docs(ChannelMetadataGuildMainBase._precreate)
    def _precreate(cls, keyword_parameters):
        self = super(ChannelMetadataGuildForum, cls)._precreate(keyword_parameters)
        
        # available_tags
        try:
            available_tags = keyword_parameters.pop('available_tags')
        except KeyError:
            pass
        else:
            available_tags = validate_available_tags(available_tags)
            self.available_tags = available_tags
        
        
        # default_thread_auto_archive_after
        try:
            default_thread_auto_archive_after = keyword_parameters.pop('default_auto_archive_duration')
        except KeyError:
            pass
        else:
            default_thread_auto_archive_after = preconvert_int_options(
                default_thread_auto_archive_after,
                'default_thread_auto_archive_after',
                AUTO_ARCHIVE_OPTIONS,
            )
            
            self.default_thread_auto_archive_after = default_thread_auto_archive_after
        
        # default_thread_reaction
        try:
            default_thread_reaction = keyword_parameters.pop('default_thread_reaction')
        except KeyError:
            pass
        else:
            if (default_thread_reaction is not None) and (not isinstance(default_thread_reaction, Emoji)):
                raise TypeError(
                    f'`default_thread_reaction` can be `None`, `{Emoji.__name__}`, '
                    f'got {default_thread_reaction.__class__.__name__}; {default_thread_reaction!r}.'
                )
            
            self.default_thread_reaction = default_thread_reaction
        
        # default_thread_slowmode
        try:
            default_thread_slowmode = keyword_parameters.pop('default_thread_slowmode')
        except KeyError:
            pass
        else:
            default_thread_slowmode = preconvert_int(default_thread_slowmode, 'default_thread_slowmode', 0, 21600)
            self.default_thread_slowmode = default_thread_slowmode
        
        # flags
        try:
            flags = keyword_parameters.pop('flags')
        except KeyError:
            pass
        else:
            flags = preconvert_flag(flags, 'flags', ChannelFlag)
            self.flags = flags
        
        # topic
        try:
            topic = keyword_parameters.pop('topic')
        except KeyError:
            pass
        else:
            if (topic is not None):
                topic = preconvert_str(topic, 'topic', 0, 1024)
                if topic:
                    self.topic = topic
        
        return self
    
    
    @copy_docs(ChannelMetadataGuildMainBase._to_data)
    def _to_data(self):
        data = ChannelMetadataGuildMainBase._to_data(self)
        
        # available_tags
        available_tags = self.available_tags
        if (available_tags is None):
            available_tag_array = []
        else:
            available_tag_array = [tag.to_data() for tag in available_tags]
        data['available_tags'] = available_tag_array
        
        # default_auto_archive_duration
        data['default_auto_archive_duration'] = self.default_thread_auto_archive_after // 60
        
        # default_thread_reaction
        default_thread_reaction = self.default_thread_reaction
        if (default_thread_reaction is None):
            default_thread_reaction_data = None
        else:
            default_thread_reaction_data = put_exclusive_emoji_data_into(default_thread_reaction, {})
        data['default_reaction_emoji'] = default_thread_reaction_data
        
        # default_thread_slowmode
        default_thread_slowmode = self.default_thread_slowmode
        if default_thread_slowmode == 0:
            default_thread_slowmode = None
        data['default_thread_rate_limit_per_user'] = default_thread_slowmode
        
        # flags
        data['flags'] = self.flags
        
        # topic
        data['topic'] = self.topic
        
        return data
