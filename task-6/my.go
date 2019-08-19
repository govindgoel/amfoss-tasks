package main

import (
    "flag"
    "fmt"
    "github.com/dghubble/go-twitter/twitter"
    "github.com/dghubble/oauth1"
    "os"
)

func main() {

    twitterHandle := flag.String("twitterHandle", "govindgoel82", "twitter handle of a user")
    flag.Parse()
    config := oauth1.NewConfig("kpM9WEJub7gswuzjU3gT7lRVH", "L8TKi5m470NaamoINjUmddqOU6LvTyKbXoxMfjXUo5FViViggl")
    token := oauth1.NewToken("717715117429751808-agCncBg0v3lofacGi9dpvttE3MSLarF", "FuRlgF1WUwQy1Y88Io7o52xIue1JlLPkBpEfM8RdAp4SD")
    httpClient := config.Client(oauth1.NoContext, token)
    client := twitter.NewClient(httpClient)
    f, err := os.Create("twitterHandles.txt")

    params := &twitter.FollowerListParams{
        ScreenName: *twitterHandle,
    }
    
    followers, resp, err := client.Followers.List(params)
    var count int = 0;
    fmt.Println(resp, err)
    f.WriteString("Followers for twitter Handle - " + *twitterHandle)
    for _, follower := range followers.Users {
        count++
        f.WriteString("\n" + follower.ScreenName)
    }
    f.WriteString("\n")
    f.WriteString(fmt.Sprintf("Total Count - %d\n", count))
    f.Close()
}
