
code present files => core ( contant/__init__.py , util/configuration_util.py ,)
                      contact_info (__init__.py , task/raw/ci_autolader_task.py )
                      setup.py , main.py

python main.py we.piple.contact_info.task.raw.ci_autoloader_task -e dev -p feature
python main.py we.piple.contact_info.task.raw.ci_autoloader_task --env dev --space feature
python main.py we.piple.contact_info.task.raw.ci_autoloader_task -e dev -p feature -b first_bucket -c feature.bronze.neustar -I 20240609 -n 8
python main.py we.piple.contact_info.task.raw.ci_autoloader_task --env dev --space feature --bucket first_bucket --catalog feature.bronze.neustar --batch-id-column batch_id --batches 8






