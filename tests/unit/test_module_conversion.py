"""Tests for hypothesis_protobuf/module_conversion.py"""

from __future__ import absolute_import, unicode_literals

from numbers import Number

from hypothesis import strategies as st

from .test_schemas import im_pb2
from .test_schemas import loop_pb2
from .test_schemas import sfixed_pb2

from hypothesis import given

from protohype.module_conversion import modules_to_strategies
from protohype.utils import full_field_name


@given(modules_to_strategies(im_pb2)[im_pb2.InstantMessage])
def test_instant_message(instant_message_example):
    assert isinstance(instant_message_example.timestamp, Number)
    assert isinstance(instant_message_example.sender.screen_name, str)
    assert isinstance(instant_message_example.recipient.screen_name, str)
    assert isinstance(instant_message_example.message, str)
    assert isinstance(instant_message_example.metadata.latency, float)
    assert isinstance(instant_message_example.metadata.inner.a, float)
    assert isinstance(
        instant_message_example.metadata.inner.layer.client.name, str
    )
    assert isinstance(instant_message_example.metadata.inner.layer.status, Number)
    assert isinstance(instant_message_example.client, Number)


test_im_strategy = modules_to_strategies(
    im_pb2,
    **{full_field_name(im_pb2.InstantMessage, "message"): st.just("test message")}
)
@given(test_im_strategy[im_pb2.InstantMessage])
def test_overrides_respected(instant_message_example):
    """Ensure provided overrides are respected."""
    assert instant_message_example.message == "test message"


@given(modules_to_strategies(im_pb2)[im_pb2.MetaData.Inner])
def test_nested_strategies_produce_data(im_example):
    """Ensure nested messages are accessible within strategy dict."""
    assert im_example

@given(modules_to_strategies(im_pb2)[im_pb2.MetaData.Inner.LimboDreamLayer])
def test_nested_strategies_produce_data(im_example):
    """Ensure twice nested messages are accessible within strategy dict."""
    assert im_example


@given(modules_to_strategies(loop_pb2)[loop_pb2.Loop])
def test_recursive_strategies_produce_data(loop_example):
    """
    Ensure that we are able to construct strategies for recursive
    messages
    """
    assert loop_example


@given(modules_to_strategies(sfixed_pb2)[sfixed_pb2.Sfixed])
def test_sfixed_values_are_in_range(sfixed):
    """
    Ensure that sfixed32 and sfixed64 fields have strategies generating
    values in the range of 32 and 64 bit signed integers respectively.
    """
    assert -(1 << 31) <= sfixed.sfixed32 <= (1 << 31) - 1
    assert -(1 << 63) <= sfixed.sfixed64 <= (1 << 63) - 1
