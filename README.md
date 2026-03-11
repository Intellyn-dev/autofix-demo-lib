# autofix-demo-lib

Simple user management library used in the AutoFix live demo.

## v2.0.0 breaking change

`get_user_by_id(id)` was renamed to `fetch_user(id)`.

Consumer apps using the old name will see:
```
AttributeError: module 'autofix_demo_lib' has no attribute 'get_user_by_id'
```
