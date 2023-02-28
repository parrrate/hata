__all__ = ('ApplicationCommandOptionMetadataChannel',)

from scarletio import copy_docs

from .fields import parse_channel_types, put_channel_types_into, validate_channel_types
from .parameter import ApplicationCommandOptionMetadataParameter


class ApplicationCommandOptionMetadataChannel(ApplicationCommandOptionMetadataParameter):
    """
    Channel parameter application command option metadata.
    
    Parameters
    ----------
    channel_types : `None`, `tuple` of ``ChannelType``
        The accepted channel types by the option.
    
    required : `bool`
        Whether the parameter is required. Defaults to `False`.
    """
    __slots__ = ('channel_types',)
    
    @copy_docs(ApplicationCommandOptionMetadataParameter.__new__)
    def __new__(cls, keyword_parameters):
        # channel_types
        try:
            channel_types = keyword_parameters.pop('channel_types')
        except KeyError:
            channel_types = None
        else:
            channel_types = validate_channel_types(channel_types)
        
        # Construct
        new = ApplicationCommandOptionMetadataParameter.__new__(cls, keyword_parameters)
        new.channel_types = channel_types
        return new
    
    
    @classmethod
    @copy_docs(ApplicationCommandOptionMetadataParameter.from_data)
    def from_data(cls, data):
        self = super(ApplicationCommandOptionMetadataChannel, cls).from_data(data)
        self.channel_types = parse_channel_types(data)
        return self
    
    
    @copy_docs(ApplicationCommandOptionMetadataParameter.to_data)
    def to_data(self, *, defaults = False):
        data = ApplicationCommandOptionMetadataParameter.to_data(self, defaults = defaults)
        put_channel_types_into(self.channel_types, data, defaults)
        return data
    
    
    @copy_docs(ApplicationCommandOptionMetadataParameter._add_type_specific_repr_fields)
    def _add_type_specific_repr_fields(self, repr_parts):
        ApplicationCommandOptionMetadataParameter._add_type_specific_repr_fields(self, repr_parts)
        
        repr_parts.append(', channel_types = ')
        repr_parts.append(repr(self.channel_types))
    
    
    @copy_docs(ApplicationCommandOptionMetadataParameter._is_equal_same_type)
    def _is_equal_same_type(self, other):
        if not ApplicationCommandOptionMetadataParameter._is_equal_same_type(self, other):
            return False
        
        if self.channel_types != other.channel_types:
            return False
        
        return True
    
    
    @copy_docs(ApplicationCommandOptionMetadataParameter.__hash__)
    def __hash__(self):
        hash_value = ApplicationCommandOptionMetadataParameter.__hash__(self)
        
        # channel_types
        channel_types = self.channel_types
        if (channel_types is not None):
            hash_value ^= len(channel_types) << 12
            
            for channel_type in channel_types:
                hash_value ^= hash(channel_type)
        
        return hash_value
    
    
    @copy_docs(ApplicationCommandOptionMetadataParameter.copy)
    def copy(self):
        new = ApplicationCommandOptionMetadataParameter.copy(self)
        
        channel_types = self.channel_types
        if (channel_types is not None):
            channel_types = (*channel_types,)
        new.channel_types = channel_types
        
        return new
    
    
    @copy_docs(ApplicationCommandOptionMetadataParameter.copy_with)
    def copy_with(self, keyword_parameters):
        # channel_types
        try:
            channel_types = keyword_parameters.pop('channel_types')
        except KeyError:
            channel_types = self.channel_types
            if (channel_types is not None):
                channel_types = (*channel_types,)
        else:
            channel_types = validate_channel_types(channel_types)
        
        # Construct
        new = ApplicationCommandOptionMetadataParameter.copy_with(self, keyword_parameters)
        new.channel_types = channel_types
        return new
