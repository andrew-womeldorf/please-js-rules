filegroup(
    name = "js",
    srcs = ["js.build_defs"],
    visibility = ["PUBLIC"],
)

python_binary(
    name = "yarn_to_please",
    main = "yarn_to_please.py",
)

python_binary(
    name = "lib_merge",
    main = "lib_merge.py",
    srcs = ["utils.py"],
)

python_binary(
    name = "yarn_binary_py",
    main = "yarn_binary.py",
    srcs = ["utils.py"],
)

python_test(
    name = "test_lib_merge",
    srcs = ["lib_merge_test.py"],
    deps = [":lib_merge"],
)

sh_binary(
    name = "yarn_binary",
    main = "yarn_binary.sh",
)
