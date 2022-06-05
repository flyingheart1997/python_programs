class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_parents(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        space = ' ' * self.get_parents() * 3
        prefix = space + '|__' if self.parent else ''
        print(prefix + self.data)
        for child in self.children:
            child.print_tree()


def build_product_tree():
    root = TreeNode('Electronics')
    laptop = TreeNode('laptop')
    laptop.add_child(TreeNode('dell'))
    laptop.add_child(TreeNode('hp'))
    laptop.add_child(TreeNode('asus'))
    
    cell_phone = TreeNode('Cell Phone')
    cell_phone.add_child(TreeNode('oppo'))
    cell_phone.add_child(TreeNode('vivo'))
    cell_phone.add_child(TreeNode('samsung'))
    root.add_child(laptop)
    root.add_child(cell_phone)
    root.print_tree()


if __name__ == '__main__':
    build_product_tree()
