/**
 * Mimic elvis-operator, but use a lambda rather than an expression.
 */
infix fun <T> T?.orIfNull(block: () -> T): T = this ?: block()
