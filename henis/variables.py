from collections import defaultdict, Counter, deque, namedtuple
import sys

class Variables:
    def __init__(self):
        self.vGraph = defaultdict(list)

    def set(self, var, val):
        try:
            if val in self.vGraph:
                nval = self.vGraph[val]
                
                self.vGraph[var] = nval
        
            else:
                self.vGraph[var] = val
        except Exception as e:
            print(e)

    
    def delete(self, var):
        """Delete a variable."""
        
        if var in self.vGraph:
            del self.vGraph[var]
            self._release_memory(var)
        else:
            print(f"Variable '{var}' not found.")

    def _track_memory(self, var):
        """Track the memory usage of the variable."""
        size = sys.getsizeof(self.vGraph[var])
        print(f"Memory allocated for variable '{var}': {size} bytes")

    def _release_memory(self, var):
        """Release the memory used by the variable."""
        # Simply calling del removes the reference to the variable in Python.
        # Python will handle the actual deallocation when the object is no longer referenced.
        print(f"Memory released for variable '{var}'.")

    def get(self, var):
        """Get the value of a variable."""
        return self.vGraph.get(var, "Variable not found.")
    
    def show_all(self):
        """Show all stored variables."""
        return self.vGraph


if __name__=="__main__":
    vars = Variables()

    # Set variables
    vars.set('a', 10+3/4-3)
    vars.set('b', [1, 2, 3])
    vars.set('c', 'a')

    # Get memory usage
    print(vars.show_all())

    print(vars.get('c'))
    print(vars.get('a'))
    # Delete a variable
    vars.delete('b')

    # Show memory after deletion
    vars.show_all()
        
    print(vars.get('b'))
