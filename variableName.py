bool variableName(std::string name) {

    if (isdigit(name[0])) return false;

    for (char c:name)
    {
        if (isdigit(c))continue;
        if( isalpha(c))continue;
        if (c=='_')continue;
        else return false;
    }
    return true;
}
