| Issue | Type | Line(s) | Description | Fix Approach |
|--------|------|----------|--------------|---------------|
| Mutable default arg | Bug | 4 | log=[] is shared across calls | Change default to None and initialize inside function |
| Broad print-based error | Logic | 15 | Using print instead of proper error handling | Use logging or raise specific Exception |
| Missing input validation | Security | 9 | User input not validated | Add checks for name, quantity, and price |
| No main guard logging | Quality | 22 | Missing logging configuration | Add logging setup for clean output |
