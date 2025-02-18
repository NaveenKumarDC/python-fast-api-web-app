db.createUser({
    user: "prd_user",
    pwd: passwordPrompt(),
    roles: ["root"]
})


db.createUser({
    user: "prd_user",
    pwd: passwordPrompt(),
    roles: [
        {
        role :"root",
        db : "prd_1"
        }
    ]
})


db.createUser({
    user: "prd_user",
    pwd: "prd_user",
    db : "prd_user",
    roles: [
        {
        role :'root',
        db : 'prd_1'
        }
    ]
})


db.createUser({
  user: "prd_user",
  pwd: "prd_user",
  roles: [
    { role: "readWrite", db: "prd_1" }
  ]
});