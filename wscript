# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-
from waflib import Logs, Utils, Context

def options(opt):
    opt.load(['compiler_cxx', 'gnu_dirs'])
    opt.load(['boost', 'unix-socket', 'dependency-checker',
              'default-compiler-flags', 'coverage' ],
             tooldir=['.waf-tools'])

def configure(conf):
    conf.load(['compiler_cxx', 'gnu_dirs',
               'default-compiler-flags',
               'boost'])

    conf.check_cfg(package='libndn-cxx', args=['--cflags', '--libs'],
                   uselib_store='NDN_CXX', mandatory=True)

    boost_libs = 'system'

    conf.check_boost(lib=boost_libs)
    if conf.env.BOOST_VERSION_NUMBER < 104800:
        Logs.error("Minimum required boost version is 1.48.0")
        Logs.error("Please upgrade your distribution or install custom boost libraries" +
                   " (http://redmine.named-data.net/projects/nfd/wiki/Boost_FAQ)")
        return


def build(bld):


    bld(target='ndnTestbedDataCollectorCmd',
      features='cxx cxxprogram',
      source='ndnTestbedDataCollectorCmd.cpp',
      use='BOOST NDN_CXX LIBRT LIBRESOLV LEXPAT',
      lib='ndn-cxx boost_random',
      )

    bld(target='ndnTestbedDataCollectorServer',
      features='cxx cxxprogram',
      source='ndnTestbedDataCollectorServer.cpp',
      use='BOOST NDN_CXX LIBRT LIBRESOLV LEXPAT',
      lib='ndn-cxx boost_random',
      )

    bld(target='ndnTestbedDataCollectorClient',
      features='cxx cxxprogram',
      source='ndnTestbedDataCollectorClient.cpp',
      use='BOOST NDN_CXX LIBRT LIBRESOLV LEXPAT',
      lib='ndn-cxx boost_random',
      )
