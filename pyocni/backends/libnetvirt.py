# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info

if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp

        fp = None
        try:
            fp, pathname, description = imp.find_module('_libnetvirt', [dirname(__file__)])
        except ImportError:
            import _libnetvirt

            return _libnetvirt
        if fp is not None:
            try:
                _mod = imp.load_module('_libnetvirt', fp, pathname, description)
            finally:
                fp.close()
            return _mod

    _libnetvirt = swig_import_helper()
    del swig_import_helper
else:
    import _libnetvirt
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method: return method(self, value)
    if (not static) or hasattr(self, name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method: return method(self)
    raise AttributeError(name)


def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object: pass

    _newclass = 0

DRIVER_OF_NOX = _libnetvirt.DRIVER_OF_NOX
DRIVER_MPLS = _libnetvirt.DRIVER_MPLS
MAX_NAME_SIZE = _libnetvirt.MAX_NAME_SIZE

class endpoint(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, endpoint, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, endpoint, name)
    __repr__ = _swig_repr
    __swig_setmethods__["uuid"] = _libnetvirt.endpoint_uuid_set
    __swig_getmethods__["uuid"] = _libnetvirt.endpoint_uuid_get
    if _newclass: uuid = _swig_property(_libnetvirt.endpoint_uuid_get, _libnetvirt.endpoint_uuid_set)
    __swig_setmethods__["swId"] = _libnetvirt.endpoint_swId_set
    __swig_getmethods__["swId"] = _libnetvirt.endpoint_swId_get
    if _newclass: swId = _swig_property(_libnetvirt.endpoint_swId_get, _libnetvirt.endpoint_swId_set)
    __swig_setmethods__["port"] = _libnetvirt.endpoint_port_set
    __swig_getmethods__["port"] = _libnetvirt.endpoint_port_get
    if _newclass: port = _swig_property(_libnetvirt.endpoint_port_get, _libnetvirt.endpoint_port_set)
    __swig_setmethods__["mpls"] = _libnetvirt.endpoint_mpls_set
    __swig_getmethods__["mpls"] = _libnetvirt.endpoint_mpls_get
    if _newclass: mpls = _swig_property(_libnetvirt.endpoint_mpls_get, _libnetvirt.endpoint_mpls_set)
    __swig_setmethods__["vlan"] = _libnetvirt.endpoint_vlan_set
    __swig_getmethods__["vlan"] = _libnetvirt.endpoint_vlan_get
    if _newclass: vlan = _swig_property(_libnetvirt.endpoint_vlan_get, _libnetvirt.endpoint_vlan_set)
    __swig_setmethods__["pad"] = _libnetvirt.endpoint_pad_set
    __swig_getmethods__["pad"] = _libnetvirt.endpoint_pad_get
    if _newclass: pad = _swig_property(_libnetvirt.endpoint_pad_get, _libnetvirt.endpoint_pad_set)

    def __init__(self):
        this = _libnetvirt.new_endpoint()
        try: self.this.append(this)
        except: self.this = this

    __swig_destroy__ = _libnetvirt.delete_endpoint
    __del__ = lambda self: None;

endpoint_swigregister = _libnetvirt.endpoint_swigregister
endpoint_swigregister(endpoint)

class constraint(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, constraint, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, constraint, name)
    __repr__ = _swig_repr
    __swig_setmethods__["src"] = _libnetvirt.constraint_src_set
    __swig_getmethods__["src"] = _libnetvirt.constraint_src_get
    if _newclass: src = _swig_property(_libnetvirt.constraint_src_get, _libnetvirt.constraint_src_set)
    __swig_setmethods__["dst"] = _libnetvirt.constraint_dst_set
    __swig_getmethods__["dst"] = _libnetvirt.constraint_dst_get
    if _newclass: dst = _swig_property(_libnetvirt.constraint_dst_get, _libnetvirt.constraint_dst_set)
    __swig_setmethods__["minBW"] = _libnetvirt.constraint_minBW_set
    __swig_getmethods__["minBW"] = _libnetvirt.constraint_minBW_get
    if _newclass: minBW = _swig_property(_libnetvirt.constraint_minBW_get, _libnetvirt.constraint_minBW_set)
    __swig_setmethods__["maxBW"] = _libnetvirt.constraint_maxBW_set
    __swig_getmethods__["maxBW"] = _libnetvirt.constraint_maxBW_get
    if _newclass: maxBW = _swig_property(_libnetvirt.constraint_maxBW_get, _libnetvirt.constraint_maxBW_set)

    def __init__(self):
        this = _libnetvirt.new_constraint()
        try: self.this.append(this)
        except: self.this = this

    __swig_destroy__ = _libnetvirt.delete_constraint
    __del__ = lambda self: None;

constraint_swigregister = _libnetvirt.constraint_swigregister
constraint_swigregister(constraint)

class fnsDesc(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, fnsDesc, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, fnsDesc, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _libnetvirt.fnsDesc_name_set
    __swig_getmethods__["name"] = _libnetvirt.fnsDesc_name_get
    if _newclass: name = _swig_property(_libnetvirt.fnsDesc_name_get, _libnetvirt.fnsDesc_name_set)
    __swig_setmethods__["uuid"] = _libnetvirt.fnsDesc_uuid_set
    __swig_getmethods__["uuid"] = _libnetvirt.fnsDesc_uuid_get
    if _newclass: uuid = _swig_property(_libnetvirt.fnsDesc_uuid_get, _libnetvirt.fnsDesc_uuid_set)
    __swig_setmethods__["nEp"] = _libnetvirt.fnsDesc_nEp_set
    __swig_getmethods__["nEp"] = _libnetvirt.fnsDesc_nEp_get
    if _newclass: nEp = _swig_property(_libnetvirt.fnsDesc_nEp_get, _libnetvirt.fnsDesc_nEp_set)
    __swig_setmethods__["nCons"] = _libnetvirt.fnsDesc_nCons_set
    __swig_getmethods__["nCons"] = _libnetvirt.fnsDesc_nCons_get
    if _newclass: nCons = _swig_property(_libnetvirt.fnsDesc_nCons_get, _libnetvirt.fnsDesc_nCons_set)
    __swig_setmethods__["forwarding"] = _libnetvirt.fnsDesc_forwarding_set
    __swig_getmethods__["forwarding"] = _libnetvirt.fnsDesc_forwarding_get
    if _newclass: forwarding = _swig_property(_libnetvirt.fnsDesc_forwarding_get, _libnetvirt.fnsDesc_forwarding_set)
    __swig_getmethods__["data"] = _libnetvirt.fnsDesc_data_get
    if _newclass: data = _swig_property(_libnetvirt.fnsDesc_data_get)

    def __init__(self):
        this = _libnetvirt.new_fnsDesc()
        try: self.this.append(this)
        except: self.this = this

    __swig_destroy__ = _libnetvirt.delete_fnsDesc
    __del__ = lambda self: None;

fnsDesc_swigregister = _libnetvirt.fnsDesc_swigregister
fnsDesc_swigregister(fnsDesc)

class libnetvirt_ops(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, libnetvirt_ops, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, libnetvirt_ops, name)
    __repr__ = _swig_repr
    __swig_setmethods__["connect"] = _libnetvirt.libnetvirt_ops_connect_set
    __swig_getmethods__["connect"] = _libnetvirt.libnetvirt_ops_connect_get
    if _newclass: connect = _swig_property(_libnetvirt.libnetvirt_ops_connect_get,
        _libnetvirt.libnetvirt_ops_connect_set)
    __swig_setmethods__["add_fns"] = _libnetvirt.libnetvirt_ops_add_fns_set
    __swig_getmethods__["add_fns"] = _libnetvirt.libnetvirt_ops_add_fns_get
    if _newclass: add_fns = _swig_property(_libnetvirt.libnetvirt_ops_add_fns_get,
        _libnetvirt.libnetvirt_ops_add_fns_set)
    __swig_setmethods__["instantiate_fns"] = _libnetvirt.libnetvirt_ops_instantiate_fns_set
    __swig_getmethods__["instantiate_fns"] = _libnetvirt.libnetvirt_ops_instantiate_fns_get
    if _newclass: instantiate_fns = _swig_property(_libnetvirt.libnetvirt_ops_instantiate_fns_get,
        _libnetvirt.libnetvirt_ops_instantiate_fns_set)
    __swig_setmethods__["remove_fns"] = _libnetvirt.libnetvirt_ops_remove_fns_set
    __swig_getmethods__["remove_fns"] = _libnetvirt.libnetvirt_ops_remove_fns_get
    if _newclass: remove_fns = _swig_property(_libnetvirt.libnetvirt_ops_remove_fns_get,
        _libnetvirt.libnetvirt_ops_remove_fns_set)
    __swig_setmethods__["modify_fns_add"] = _libnetvirt.libnetvirt_ops_modify_fns_add_set
    __swig_getmethods__["modify_fns_add"] = _libnetvirt.libnetvirt_ops_modify_fns_add_get
    if _newclass: modify_fns_add = _swig_property(_libnetvirt.libnetvirt_ops_modify_fns_add_get,
        _libnetvirt.libnetvirt_ops_modify_fns_add_set)
    __swig_setmethods__["modify_fns_del"] = _libnetvirt.libnetvirt_ops_modify_fns_del_set
    __swig_getmethods__["modify_fns_del"] = _libnetvirt.libnetvirt_ops_modify_fns_del_get
    if _newclass: modify_fns_del = _swig_property(_libnetvirt.libnetvirt_ops_modify_fns_del_get,
        _libnetvirt.libnetvirt_ops_modify_fns_del_set)
    __swig_setmethods__["stop"] = _libnetvirt.libnetvirt_ops_stop_set
    __swig_getmethods__["stop"] = _libnetvirt.libnetvirt_ops_stop_get
    if _newclass: stop = _swig_property(_libnetvirt.libnetvirt_ops_stop_get, _libnetvirt.libnetvirt_ops_stop_set)
    __swig_setmethods__["request_ids"] = _libnetvirt.libnetvirt_ops_request_ids_set
    __swig_getmethods__["request_ids"] = _libnetvirt.libnetvirt_ops_request_ids_get
    if _newclass: request_ids = _swig_property(_libnetvirt.libnetvirt_ops_request_ids_get,
        _libnetvirt.libnetvirt_ops_request_ids_set)

    def __init__(self):
        this = _libnetvirt.new_libnetvirt_ops()
        try: self.this.append(this)
        except: self.this = this

    __swig_destroy__ = _libnetvirt.delete_libnetvirt_ops
    __del__ = lambda self: None;

libnetvirt_ops_swigregister = _libnetvirt.libnetvirt_ops_swigregister
libnetvirt_ops_swigregister(libnetvirt_ops)

class libnetvirt_info(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, libnetvirt_info, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, libnetvirt_info, name)
    __repr__ = _swig_repr
    __swig_setmethods__["driver"] = _libnetvirt.libnetvirt_info_driver_set
    __swig_getmethods__["driver"] = _libnetvirt.libnetvirt_info_driver_get
    if _newclass: driver = _swig_property(_libnetvirt.libnetvirt_info_driver_get,
        _libnetvirt.libnetvirt_info_driver_set)
    __swig_setmethods__["ops"] = _libnetvirt.libnetvirt_info_ops_set
    __swig_getmethods__["ops"] = _libnetvirt.libnetvirt_info_ops_get
    if _newclass: ops = _swig_property(_libnetvirt.libnetvirt_info_ops_get, _libnetvirt.libnetvirt_info_ops_set)

    def __init__(self):
        this = _libnetvirt.new_libnetvirt_info()
        try: self.this.append(this)
        except: self.this = this

    __swig_destroy__ = _libnetvirt.delete_libnetvirt_info
    __del__ = lambda self: None;

libnetvirt_info_swigregister = _libnetvirt.libnetvirt_info_swigregister
libnetvirt_info_swigregister(libnetvirt_info)


def libnetvirt_init(*args):
    return _libnetvirt.libnetvirt_init(*args)

libnetvirt_init = _libnetvirt.libnetvirt_init

def libnetvirt_stop(*args):
    return _libnetvirt.libnetvirt_stop(*args)

libnetvirt_stop = _libnetvirt.libnetvirt_stop

def libnetvirt_connect(*args):
    return _libnetvirt.libnetvirt_connect(*args)

libnetvirt_connect = _libnetvirt.libnetvirt_connect

def libnetvirt_disconnect(*args):
    return _libnetvirt.libnetvirt_disconnect(*args)

libnetvirt_disconnect = _libnetvirt.libnetvirt_disconnect

def libnetvirt_create_fns(*args):
    return _libnetvirt.libnetvirt_create_fns(*args)

libnetvirt_create_fns = _libnetvirt.libnetvirt_create_fns

def libnetvirt_modify_fns_add(*args):
    return _libnetvirt.libnetvirt_modify_fns_add(*args)

libnetvirt_modify_fns_add = _libnetvirt.libnetvirt_modify_fns_add

def libnetvirt_modify_fns_del(*args):
    return _libnetvirt.libnetvirt_modify_fns_del(*args)

libnetvirt_modify_fns_del = _libnetvirt.libnetvirt_modify_fns_del

def libnetvirt_remove_fns(*args):
    return _libnetvirt.libnetvirt_remove_fns(*args)

libnetvirt_remove_fns = _libnetvirt.libnetvirt_remove_fns

def libnetvirt_request_ids(*args):
    return _libnetvirt.libnetvirt_request_ids(*args)

libnetvirt_request_ids = _libnetvirt.libnetvirt_request_ids

def parse_fns(*args):
    return _libnetvirt.parse_fns(*args)

parse_fns = _libnetvirt.parse_fns

def parse_fns_Mem(*args):
    return _libnetvirt.parse_fns_Mem(*args)

parse_fns_Mem = _libnetvirt.parse_fns_Mem

def add_local_epoint(*args):
    return _libnetvirt.add_local_epoint(*args)

add_local_epoint = _libnetvirt.add_local_epoint

def create_local_fns(*args):
    return _libnetvirt.create_local_fns(*args)

create_local_fns = _libnetvirt.create_local_fns

def printFNS(*args):
    return _libnetvirt.printFNS(*args)

printFNS = _libnetvirt.printFNS

def getEndpoint(*args):
    return _libnetvirt.getEndpoint(*args)

getEndpoint = _libnetvirt.getEndpoint


