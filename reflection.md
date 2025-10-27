### Reflection

**Easiest issues to fix:**  
Style errors like missing spaces or docstrings — they are easy to identify and correct.

**Hardest issues:**  
Mutable default arguments and Bandit security warnings required more understanding.

**False positives:**  
Bandit sometimes flags normal print usage as a security concern, which was not harmful in this case.

**How to integrate these tools:**  
In real projects, I would use these tools in a GitHub Action workflow or pre-commit hooks to automatically analyze code before merging.

**Improvements observed:**  
After fixing issues, the code became cleaner, safer, and easier to maintain.
