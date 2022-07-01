#!/usr/bin/python

# Copied from https://eengstrom.github.io/musings/add-bitwise-operations-to-ansible-jinja2

# Add some bitwise filters to ansible / jinja2; deemed not essential:
#  - https://github.com/pallets/jinja/issues/249
# Basic filter intro example:
#  - https://dev.to/aaronktberry/creating-custom-ansible-filters-29kf


class FilterModule(object):
    def filters(self):
        return {
            'bitwise_and': self.bitwise_and,
            'bitwise_or': self.bitwise_or,
            'bitwise_xor': self.bitwise_xor,
            'bitwise_complement': self.bitwise_complement,
            'bitwise_shift_left': self.bitwise_shift_left,
            'bitwise_shift_right': self.bitwise_shift_right,
        }

    def bitwise_and(self, x, y):
        return x & y

    def bitwise_or(self, x, y):
        return x | y

    def bitwise_xor(self, y, x):
        return x ^ y

    def bitwise_complement(self, x):
        return ~x

    def bitwise_shift_left(self, x, b):
        return x << b

    def bitwise_shift_right(self, x, b):
        return x >> b
