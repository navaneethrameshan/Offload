import controller
import nodelist
import db

if __name__ == '__main__':
    controller.update_node_list()
    nodes = nodelist.get_node_list()
    bucket = db.Database("test")
    bucket.get_node_data_time_range(nodes, "2013-04-07", "2013-05-11")